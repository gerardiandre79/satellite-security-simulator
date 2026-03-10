import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect("broker",1883)

def send_telemetry():

    client.publish("satellite/telemetry","altitude=400km")

while True:
    send_telemetry()