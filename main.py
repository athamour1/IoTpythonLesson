import paho.mqtt.client as mqtt
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Button
# from threading import Timer
# from datetime import datetime
import ssl
import os
import sys

class IoTExample:
    def __init__(self):
        self._establish_mqtt_connection()
    # call this method to start the client loop
    def start(self):
        self.client.loop_forever()
    # call this method to disconnect from the broker
    def disconnect(self, args=None):
        self.client.disconnect()
    # disconnect
    def _establish_mqtt_connection(self):
        print('Successful connection')
        client.subscribe('hscnl/hscnl02/state/ZWaveNode005_Switch/state')
    def _on_connect(self, client, userdata, flags, rc):
        print('I need to be completed')
    def _on_message(self, client, userdata, msg):
        print(msg.topic+' '+str(msg.payload))
    def _on_log(self, client, userdata, level, buf):
        print('log: ', buf)
try:
    iot_example = IoTExample()
    iot_example.start()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        iot_example.disconnect()
        sys.exit(0)
    except SystemExit:
        os._exit(0)