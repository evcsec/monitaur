from .date import get_current_datetime
import os, time

def write_log(host_name, msg_type, error_string):
    # Is file already open?
    log_file = "log/" + host_name + ".log"

    if os.path.exists(log_file):
        try:
            os.rename(log_file, log_file)
            with open(log_file, "a") as log:
                log.write(host_name + ',' + str(get_current_datetime()) + ',' + msg_type + ',' + str(error_string) +'\n')
                log.close()
        except OSError as e:
            print("[-] Error: File is already open... waiting until available...")
    else:
        # Wait 5 seconds... then try again
        time.sleep(5)
        with open(log_file, "a") as log:
            log.write(host_name + ',' + str(get_current_datetime()) + ',' + msg_type + ',' + str(error_string) +'\n')
            log.close()