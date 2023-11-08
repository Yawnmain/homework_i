import time
import paho.mqtt.client as mqtt
import random

broker = "broker.emqx.io"

client = mqtt.Client()

print("Connecting to broker", broker)
client.connect(broker)
client.loop_start()
print("Publishing")

for _ in range(10):
    state = "6" if random.randint(0, 1) else "off"
    print(f'state is {state}')
    client.publish("dct/yawnmain", state)
    time.sleep(random.randint(4, 10))

client.disconnect()
client.loop_stop()