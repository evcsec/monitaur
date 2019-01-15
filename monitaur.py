#!/usr/bin/python
import sys
from lib.config import Config
from lib.input import ArgumentHandler
from lib.date import get_current_datetime, get_time_diff
from lib.scanner import start_monitor

def monitaur():
    print("hi")
    print_banner()
    config = Config()

    parser = ArgumentHandler()
    arguments = parser.parse(sys.argv[1:])
    
    start_monitor(config)

def print_banner():
    print("""                                                                                         
                                        _/    _/                                    
   _/_/_/  _/_/      _/_/    _/_/_/        _/_/_/_/    _/_/_/  _/    _/  _/  _/_/   
  _/    _/    _/  _/    _/  _/    _/  _/    _/      _/    _/  _/    _/  _/_/        
 _/    _/    _/  _/    _/  _/    _/  _/    _/      _/    _/  _/    _/  _/           
_/    _/    _/    _/_/    _/    _/  _/      _/_/    _/_/_/    _/_/_/  _/            
                                                                                    
    A web monitoring tool created by @snags141 and @evcsec
    """)

if __name__ == '__main__':
    monitaur()