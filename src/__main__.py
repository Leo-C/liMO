'''
Copyright 2017 - LC

This file is part of liMO.

liMO is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

liMO is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with liMO.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import sys
import time
import paho.mqtt.client as mqtt
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from libs.config import cfg_init, cfg_get, cfg_get_default
from libs.logutils import init_log, log
from libs.mqttutils import mqtt_init, mqtt_loop
from libs.heaputils import heap_init
from libs.timeutils import scheduler, sched_init
#from libs.scriptutils import init_plugins


class ConfigChangeHandler(FileSystemEventHandler):
    def __init__(self, config_dir):
        self.config_dir = config_dir
    
    def on_modified(self, event):
        log(4, "Config reload")
        init(self.config_dir)


def init(config_dir):
    #init config
    cfg_init(config_dir)
    
    #init log
    logl = int(cfg_get_default("LOG_LEVEL", "0"))
    logf = cfg_get_default("LOG_FILE", "")
    init_log(logl, logf)
    
    #init heap
    heap_init(config_dir)
    
    #init scheduler
    sched_init()
    
    #start MQTT client
    usr = cfg_get_default("MQTT_USER", "")
    pwd = cfg_get_default("MQTT_PASSWORD", "")
    mqtt_init(config_dir, cfg_get("MQTT_SERVER"), usr, pwd)

def start_cfg_observer(config_dir):
    #observe config changes
    event_handler = ConfigChangeHandler(config_dir)
    observer = Observer()
    observer.schedule(event_handler, config_dir, recursive=False)
    observer.start()
    
    try:
        while True:
            mqtt_loop(1)
            scheduler()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


#specify base directory as argv[1]
if __name__ == "__main__":
    if len(sys.argv) > 1:
        base_path = os.path.abspath(sys.argv[1])
        sys.path.append(base_path)
    else:
        if os.path.isabs(sys.path[0]):
            base_path = os.path.abspath(sys.path[0])
        else:
            base_path = os.path.abspath(os.getcwd())
            sys.path.append(base_path)
    config_dir = base_path + '/config'
    
    import libs.scriptutils
    init(config_dir)
    libs.scriptutils.init_plugins(config_dir)
    log(3, "MQTT orchestrator ready!")
    start_cfg_observer(config_dir)
