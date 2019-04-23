#################################################################
#
# Code by P. Marti BFH 21.04.2019
# Ecercise MQTT FS 2019
#   
#
#################################################################

import paho.mqtt.client as mqtt
# MQTT Server Information 
SERVER = "m24.cloudmqtt.com"
PORT = 15254
# User login if needed
USER ='jhkvdesg'
PW ='IRGIIMITLIg8'
# MQTT broker topic (subscribe)
TOPIC='temp_humidity'

def on_connect(client,userdata,flags,rc):
    print('connected with result code {0}'.format(rc))
    client.subscribe(TOPIC)
    
def on_message(client,userdata,msg):
    t,p=[float(x) for x in msg.payload.decode("utf-8").split(',')]
    print('{0}C     {1}mPa'.format(t,p))
    #display_data(t,h)
    
client=mqtt.Client()
client.username_pw_set(USER, PW)
client.connect(SERVER,port=PORT,keepalive=60,bind_address='0.0.0.0')
client.on_connect=on_connect
client.on_message=on_message

#client.subscribe("")
client.loop_start()
input("Press enter to terminate")
