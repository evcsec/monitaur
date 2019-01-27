from .date import get_current_datetime

def write_log(host_name, msg_type, error_string):
    log = open("monitaur.log", "a")
    log.write(host_name + ',' + str(get_current_datetime()) + ',' + msg_type + ',' + str(error_string) +'\n')
    log.close()