import requests, time
from date import get_current_datetime, get_time_diff
from config import validate_url, update_config
from logger import write_log

def start_scan(host_name, url):  
    # Initiate a scan on the given URL
    r = None
    status_code = None

    try:
        r = requests.get(url)
    except requests.exceptions.Timeout:
        error_string = "An error occured: timeout"
        write_log(host_name, 'Error', error_string)
        print(error_string)
    except requests.exceptions.TooManyRedirects:
        error_string = "An error occured: toomanyredirects"
        write_log(host_name, 'Error', error_string)
        print(error_string)
    except requests.exceptions.RequestException as e:
        print("an exception occurred")
        exception_args = e.args[0]
        error_string = str(exception_args)
        write_log(host_name, 'Error')
        print("Error = " + error_string)
        print(e)

    if r is not None:
        status_code = r.status_code
        write_log(host_name, 'Status Response', 'status_code = ' + str(status_code))

    print("Status code for " + host_name + " = " + str(status_code))

def do_scan(config):
    for each_section in config.CONFIG.sections():

        target_url = config.CONFIG.get(each_section, 'target_url')
        interval_time = config.CONFIG.get(each_section, 'interval_time')
        last_scan = config.CONFIG.get(each_section, 'last_scan')

        # debug
        print('Target URL:')
        print(target_url)
        print('Interval Time:')
        print(interval_time)
        print('Last Scan:')
        print(last_scan)

        if not validate_url(target_url):
            print('Error: URL %s' % target_url + ' is not valid')
            break  # Quit program, config must have been changed outside of program

        if interval_time == '':
            print('Error: not configured properly for %s' % target_url)
            print('Missing interval_time. Please amend the config.ini file to reflect the interval time...')
            break  # Quit program, config must have been changed outside of program

        if last_scan == '':
            start_scan(each_section, target_url)
            update_config(config, each_section, target_url, interval_time, get_current_datetime())
        else:
            if int(get_time_diff(last_scan)) >= int(interval_time):
                start_scan(each_section, target_url)
                update_config(config, each_section, target_url, interval_time, get_current_datetime())

def start_monitor(config):  # Start monitoring the target URL
    while True:
        print('*Monitor started: running every 5 seconds*')
        time.sleep(5)
        do_scan(config)
        print('Waiting ...\n')