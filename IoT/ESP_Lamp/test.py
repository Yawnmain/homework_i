import time
import paho.mqtt.client as paho
import argparse

broker = "broker.emqx.io"

def on_publish(client, userdata, result):
    print("Command published")

def main(client_id):
    client = paho.Client(client_id)
    client.on_publish = on_publish

    print("Connecting to broker", broker)
    client.connect(broker)
    client.loop_start()
    print("Publishing")

    min_duration = 10
    max_duration = 40
    current_duration = max_duration

    try:
        while True:
            current_duration -= 1

            if current_duration < min_duration:
                current_duration = max_duration

            now = time.localtime()
            second_of_minute = now.tm_sec

            if min_duration <= second_of_minute <= max_duration:
                state = "0"
            else:
                state = "1"

            client.publish(f"{client_id}/command", state)
            print(f"Time: {time.strftime('%H:%M:%S', now)}, State: {state}, "
                  f"Shining from {min_duration} to {max_duration} seconds")

            time.sleep(1)

    except KeyboardInterrupt:
        client.disconnect()
        client.loop_stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Control a lamp simulation")
    parser.add_argument("client_id", help="ID of the lamp")
    args = parser.parse_args()

    main(args.client_id)
