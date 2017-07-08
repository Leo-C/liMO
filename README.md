## **li**ghtweight **M**QTT **O**rchestrator


### Introduction

**liMO** (pron. like *lee-mo*, italian word for a type of *clay*) is a lightweight MQTT orchestrator written in python.  
(see [MQTT standard](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html) or [MQTT wiki](https://github.com/mqtt/mqtt.github.io/wiki) for base MQTT concepts)  

Main concept in *liMO* are *Actions* triggered by (registered) MQTT events specified with a pseudo-scripting python-based language.


### Installation

*liMO* is multiplatform; requirements are:

* [Python 2.7.x](https://www.python.org/)
* [Paho MQTT](https://pypi.python.org/pypi/paho-mqtt/1.1)
* [Watchdog](https://pypi.python.org/pypi/watchdog)

To install additional packages *[pip]()* can be used:  
```python -m pip install paho-mqtt```  
```python -m pip install watchdog```


### Starting **liMO**

*liMO* can be started as '.zip' file:  
```python liMO.zip [<base_dir>]```  
or or from source files with command:  
```python __main__.py [<base_dir>]```  
If ```<base_dir>``` is not specified, then ```config``` directory under current directory is considered to search config files and ```plugins``` directory under current directory is considered for plugins


### Configurations

*<config_dir>* is optional and specify directory with config files;  
if not specified ```config``` directory under current directory is used.  
In config directory following files are searched:  

* ```config.properties```: configuration file with following fields:
  - ```MQTT_SERVER```: mandatory, is host of MQTT server  
  - ```MQTT_USER```: optional, is user for MQTT server
  - ```MQTT_PASSWORD```: optional, is password for MQTT server
  - ```LOG_LEVEL```: optional, is logging level. Permitted levels are:
    - 0: log none (*default*)
    - 1: log only Warnings
    - 2: log Warnings and Errors
    - 3: log Warnings, Errors and Info
    - 4: log Warnings, Errors, Info and Debug
  - ```LOG_FILE```: optional, is file to store log; if not specified is  ```STDOUT```
* ```events.properties```: specify registered actions (MQTT topic)
* ```heap.properties```: specify initial configuration stored into *heap* (see [Programming](# Programming))
* ```scripting.properties```: specify registered funtcions used in scripting language

All files are in Java properties format, with indexed values (and comments starting with '#'):  
```# Comment```  
```key=format```  


### Programming

File ```events.properties``` specify registered *actions* with following format:  
```MQTT_TOPIC=<python script>```  
where ```MQTT_TOPIC``` is a registered MQTT topic and *```<python script>```* is a single-line script executed when specified topic is received.  

Scripts run in a sand-box and can be structured as 1..n command/functions separated by ';' (like python-syntax)  using python built-ins, *liMO* [base functions](docs/scripting.md) and user-functions added as [plugin](# Plugins).  

Functions share a memory-persistent *heap* (pre-initialized with file ```heap.properties```); variables can be refernced as function parameters in scripts.  

**NOTE**: special variables valid only at __top-level__ are:  

* *TOPIC*: MQTT topic of received message  
* *PAYLOAD*: MQTT payload of received message  


### Plugins

Plugins are python files (**.py*) contained into ```<base_dir>/plugin```.  
These python files expose python functions referenced in ```scripting.properties``` configuration file with syntax:  
```<function_name_in_sandbox>=<module>.<function_name_in_py_file>```   

Note that *plugins* module (directory itself) must not be included in fully-qulified name of python funtion. E.g.:  
```len=stringutils.strlen```  
is referencing *strlen()* function into file ```stringutils.py``` (*module*) under ```<base_dir>/plugins``` directory (implicit) using it as *len()* in file ```events.properties```


### License

This program is licensed under [GPLv3](https://www.gnu.org/licenses/gpl.txt) license; no warranty is due, but you can contact me for problem and/or clarifications.  

Commercial use is granted freely, but please inform me about this.
