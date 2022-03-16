import paho.mqtt.client as mqtt

mqtt_broker = "broker.mqttdashboard.com"
mqtt_port = 1883
topic = "Test120"

def on_connect(client, userdata, flags, rc):
    print("Connected successfully") 
    client.subscribe(topic, 0)   

def on_message(client, userdata, msg):
    print(str(msg.payload.decode("utf-8")))

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)
client.on_connect = on_connect
client.on_message = on_message

client.subscribe(topic, 0)
# client.on_subscribe()

client.loop_forever()