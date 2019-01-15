import os, configparser, validators

class Config(object):
    CONFIG = configparser.ConfigParser()  # init config
    def __init__(self):
        # if doesnt exist, write default
        if not os.path.exists('./config.ini'):
            self.set_targets()
        else:
            self.CONFIG.read("./config.ini")

    def add_host(self, host, target_url, interval_time, last_scan):
        self.CONFIG[host] = {'target_url': target_url, 'interval_time': interval_time, 'last_scan': last_scan}
        self.write_file()

    def set_targets(self):
    
        while True:
            host = raw_input("Enter a name for this host\n> ")

            # Check if exists
            if self.CONFIG.has_section(host):
                print('A host with this name already exists\nPlease enter something else\n> ')
            else:
                # Create new entry
                url = raw_input('Please enter a target URL://)\n> ')
                if validators.url(url):
                    interval_time = raw_input("How long between scans? (minutes):\n> ")
            
            self.add_host(host, url, interval_time, "")

            add_more = raw_input('Would you like to add another host? (y/n)')
            if add_more.lower() != "y":
                break

    def write_file(self):
        self.CONFIG.write(open('config.ini', 'w'))
    
def print_targets(self):
    print('\nCurrent Targets:')
    # Loop through CONFIG and print section titles
    for each_section in self.CONFIG.sections():
        print(' - ' + each_section)

def update_config(config, host, target_url, interval_time, last_scan):
        config.CONFIG[host] = {'target_url': target_url, 'interval_time': interval_time,
                                'last_scan': last_scan}
        config.write_file()

def validate_url(url):
    if validators.url(url):
        return True
    else:
        return False