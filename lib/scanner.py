import requests, time, sys, threading, socket
from .date import get_current_datetime, get_time_diff
from .config import validate_url, update_config
from .logger import write_log

def port_scan(host_name, url, saved_ip):
    # Set Ports to scan
    ports = ['80', '443', '8000', '8443', '8080', '5443']

    # Configure default timeout period for port scans (float)
    socket.setdefaulttimeout(1.5)
    target_ip = socket.gethostbyname(url)
    if target_ip != saved_ip:
        error_string = ("\t[-] Error: " + host_name + " has detected an IP conflict. Original:" + saved_ip + ", New:" + target_ip)
        write_log(host_name, 'Error', error_string)
        print(error_string)
    else:
        information_string = ("[+] Host: " + host_name + " translates to " + target_ip)
        write_log(host_name, 'Information', information_string)

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target_ip, int(port)))
        if result == 0:
            print("\t[+] Host: " + host_name + " - Port {}:\tOpen".format(port))
        sock.close()
    print("[+] Host: " + host_name + " port scan has completed.")

    return target_ip

def start_scan(host_name, url):  
    # Initiate a scan on the given URL
    r = None 
    status_code = None

    try:
        r = requests.get(url)
    except requests.exceptions.Timeout:
        error_string = "[-] Error: Timeout..."
        write_log(host_name, 'Error', error_string)
        print(error_string)
    except requests.exceptions.TooManyRedirects:
        error_string = "[-] Error: Too many redirects..."
        write_log(host_name, 'Error', error_string)
        print(error_string)
    except requests.exceptions.RequestException as e:
        print("[-] Error: An exception has occurred...")
        exception_args = e.args[0]
        error_string = str(exception_args)
        write_log(host_name, 'Error', error_string)
        print("[-] Exception Error: " + error_string)
        print(e)

    if r is not None:
        status_code = r.status_code
        write_log(host_name, 'Status Response', 'status_code = ' + str(status_code))

    print("[+] Status code for " + host_name + " = " + str(status_code))

def do_scan(config, host_name, target_url, saved_ip, interval_time, last_scan):
    print('[+] Scanning: ' + target_url)

    if not validate_url('https://' + target_url):
        print('[-] Error: URL https://%s' % target_url + ' is not valid')
        complete_url = "http://" + target_url
        if not validate_url('http://' + target_url):
            print('[-] Error: URL http://%s' % target_url + ' is not valid')
            sys.exit(1)  # Quit program, config must have been changed outside of program
    else:
        complete_url = "https://" + target_url

    if interval_time == '':
        print('[-] Error: not configured properly for %s' % target_url)
        print('[-] Missing interval_time. Please amend the config.ini file to reflect the interval time...')
        sys.exit(1)  # Quit program, config must have been changed outside of program

    if last_scan == '':
        start_scan(host_name, complete_url)
        target_ip = port_scan(host_name, target_url, saved_ip)
        update_config(config, host_name, target_url, target_ip, interval_time, get_current_datetime())
        print('[+] Scan completed for ' + host_name + ', config updated with last scan...')
    else:
        if int(get_time_diff(last_scan)) >= int(interval_time):
            start_scan(host_name, complete_url)
            target_ip = port_scan(host_name, target_url, saved_ip)
            update_config(config, host_name, target_url, target_ip, interval_time, get_current_datetime())
            print('[+] Scan completed for ' + host_name + ', config updated with last scan...')
    print('[+] Sleeping until next scan...')
    time.sleep(int(interval_time)*60)

def start_monitor(config):  # Start monitoring the target URL
    threads=[]
    while True:
        print('[+] Loading sites to scan...')
        for each_section in config.CONFIG.sections():
            target_url = config.CONFIG.get(each_section, 'target_url')
            target_ip = config.CONFIG.get(each_section, 'target_ip')
            interval_time = config.CONFIG.get(each_section, 'interval_time')
            last_scan = config.CONFIG.get(each_section, 'last_scan')

            t = threading.Thread(target=do_scan, args=(config, each_section, target_url, target_ip, interval_time, last_scan))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()