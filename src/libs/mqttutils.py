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

import paho.mqtt.client as mqtt

from libs.utils import load_properties
from libs.logutils import log

EVENTS_CONFIG_FILE = 'events.properties'
mqttcl = None #MQTT client
mqttserver = None
events = {} #registered handlers


def del_subscriptions():
    global mqttcl
    if mqttcl != None:
        for k, v in events.iteritems():
            mqttcl.unsubscribe(k)

def set_subscriptions():
    global mqttcl
    if mqttcl != None:
        for k, v in events.iteritems():
            mqttcl.subscribe(k)

def mqtt_message(client, userdata, msg):
    import heaputils
    mqtt_msg = {'TOPIC': msg.topic, 'PAYLOAD': msg.payload}
    log(4, str(mqtt_msg))
    heaputils.exec_cmd(events[msg.topic], mqtt_msg)

def on_connect(client, userdata, flags, rc):
    global mqttcl
    if rc == 3: #server unreacheable
        mqttcl = mqttcl.connect(mqttserver)

def on_disconnect(client, userdata, rc):
    global mqttcl
    mqttcl = mqttcl.connect(mqttserver)

def mqtt_loop(tout):
    global mqttcl
    mqttcl.loop(timeout = tout)

def mqtt_init(config_dir, MQTTsrv, MQTTuser, MQTTpwd):
    global mqttcl
    global mqttserver
    mqttserver = MQTTsrv
    mqttcl = mqtt.Client()
    if MQTTsrv != "":
        mqttcl.username_pw_set(MQTTuser, MQTTpwd)
    mqttcl.on_message = mqtt_message
    mqttcl.on_connect = on_connect
    mqttcl.on_disconnect = on_disconnect
    mqttcl.connect(mqttserver)
    
    #log MQTT orchestrator attach
    mqtt_publish('stat/MQTTorchestrator/start', '')
    
    global events
    del_subscriptions()
    events = load_properties(config_dir + '/' + EVENTS_CONFIG_FILE)
    set_subscriptions()


def mqtt_publish(topic, payload):
    global mqttcl
    mqttcl.publish(topic, payload)
