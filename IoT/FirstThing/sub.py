import time
import paho.mqtt.client as mqtt
import serial_

responses = {
              'd':7,
              'u':6
            }

broker = 'broker.emqx.io'

def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    if data in list(responses.keys()):
        serial_.send_command(data, responses[data])
        print("received message =", data)

client = mqtt.Client()
client.on_message = on_message

client.connect(broker)
client.loop_start()
print("Subscribing")
client.subscribe("dct/yawn")
time.sleep(1800)
client.disconnect()
client.loop_stop()