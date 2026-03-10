import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect("broker",1883)

client.publish("satellite/command","shutdown")