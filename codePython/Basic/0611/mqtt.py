import paho.mqtt.client as mqtt

client = mqtt.Client()
mqtt_broker = "broker.mqttdashboard.com"
mqtt_port = 1883
topic = "Test120"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def connect():
    client.on_connect = on_connect
    client.on_message = on_message

def publish(msg):
    client.connect(mqtt_broker, mqtt_port, 60)
    client.publish(topic, str(msg), 0, False)

def main():
    connect()
    publish("Hello World!")

if __name__ == '__main__':
    main()
