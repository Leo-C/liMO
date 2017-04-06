Scripting Documentation
-----------------------
  
  
### HEAP values

* *TOPIC*: MQTT topic of received MQTT message
* *PAYLOAD*: MQTT payload of received MQTT message
  
### Scripting functions

* *mqtt(topic, payload)*: send to MQTT broker a message with specified *topic* and *payload*
* *schedule(sec, command)*: schedule a string *command* to be executed after *sec* seconds
* *schedules((sec, command), ...)*: *n* schedules can be specified as tuples (*sec*, *command*); for each tuple a *command* is scheduled after *sec* seconds
* *log(level, message)*: log (on stdout or file depending by configuration) a *message* with specified priority *level* (1=ERROR, 4=DEBUG)
* *nop()*: no-operation
* *ifte(condition, if_true, if_false)*: string commands *if_true* or *if_false* are executed respectively if evaluated *condition* string is true or false
* *ifundef(variable, value, command)*: if *variable* in unset into heap, then *variable* is set to *value* and *command* is executed
* *getdef(variable, default)*: return value of *variable* from heap (*default* if unset)
* *get(variable)*: return value of *variable* from heap (*None* if unset)
* *set(variable, value)*: set value of *variable* to *value* on heap
* *unset(variable)*: del *variable* from heap
* *substring(text, start, stop)*: extract substring of *text* from character *start* to character *stop*. If *start*=0, substring start from beginning; if *stop*=0, substring ends to finish; if *stop*<0 substring finish *stop* characters before end
* *len(text)*: return length of *text*
