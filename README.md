
# Monitaur

A multithreaded website monitoring CLI tool, used to confirm website access, open ports and detects IP changes.
This tool will be mutured to implement alerting for changes to IPs and changes to website availability.

## Authors

* **Evcsec**
* **snags141**


## Getting Started
A first run will request the configuration upfront. 
Once a config file exists, we rely on this configuration to move forward.
Configuration (config.ini) can be updated separately at this stage, but this will be changed moving forward.

### Prerequisites

Below are the main python libraries and imports currently used for the project. See Monitaur.py for full list.

```
- Requests
- Validators
```

### Installing

The script is super simple to setup. Running for the first time, or without a config file present will prompt you to set up one or more hosts to scan, and the time interval between each scan.

Although URLs are validated, Monitaur checks both http:// and https://.

