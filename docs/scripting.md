Scripting Documentation
-----------------------
  
  
### HEAP values

* *TOPIC*: MQTT topic of received MQTT message
* *PAYLOAD*: MQTT payload of received MQTT message
  
### Scripting functions

* *mqtt(topic, payload, [qos=0])*: send to MQTT broker a message with specified *topic* and *payload* and optionally *qos* value
* *mqtt_r(topic, payload, [qos=0])*: send to MQTT broker a message with specified *topic* and *payload* and optionally *qos* value, retaining message for subscribers to specified topic
* *schedule(sec, command)*: schedule a string *command* to be executed after *sec* seconds
* *schedules((sec, command), ...)*: *n* schedules can be specified as tuples (*sec*, *command*); for each tuple a *command* is scheduled after *sec* seconds
* *tonoff(id, sec_on, sec_off, command_on, command_off)*: execute *command_on* after *sec_on* seconds and *command_off* after *sec_on*+*sec_off* seconds; if another message is received before *sec_on*+*sec_off* seconds is ignored
* *mtonoff(id, (sec1, command1), (sec2, command2), ...)*: execute *command1* after *sec1* seconds from trigger, *command2* after *sec1*+*sec2* seconds and so on ...; if another message is received before end of events, then is ignored
* *log(level, message)*: log (on stdout or file depending by configuration) a *message* with specified priority *level* (1=ERROR, 4=DEBUG)
* *nop()*: no-operation
* *ifte(condition, if_true, if_false)*: string commands *if_true* or *if_false* are executed respectively if evaluated *condition* string is true or false
* *ifundef(variable, value, command)*: if *variable* in unset into heap, then *variable* is set to *value* and *command* is executed
* *lock(id)*: if a lock is unset on variable *id*, set it and return true; otherwise return false
* *unlock(id)*: if a lock is set on variable *id*, unset it; otherwise do nothing
* *getdef(variable, default)*: return value of *variable* from heap (*default* if unset)
* *get(variable)*: return value of *variable* from heap (*None* if unset)
* *set(variable, value)*: set value of *variable* to *value* on heap
* *unset(variable)*: del *variable* from heap
* *substring(text, start, stop)*: extract substring of *text* from character *start* to character *stop*. If *start*=0, substring start from beginning; if *stop*=0, substring ends to finish; if *stop*<0 substring finish *stop* characters before end
* *len(text)*: return length of *text*
