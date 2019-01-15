
# Monitaur

Monitaur is a tool to periodically detect and alert on website availability. A typical use for this would be to query multiple hosted services for availability.

## Authors

* **Evcsec**
* **snags141**


## Getting Started
A first off run and set the config file and you're off and running.

### Prerequisites

Below are the main python libraries and imports currently used for the project. See Monitaur.py for full list.

```
- Requests
- Validators
```

### Installing

The script is super simple to setup. Running for the first time, or without a config file present will prompt you to set up one or more hosts to scan, and the time interval between each scan.

Although URLs are validated, Monitaur checks both http:// and https://.

