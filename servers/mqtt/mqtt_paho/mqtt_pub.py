import paho.mqtt.client as mqtt

if __name__=='__main__':
    client = mqtt.Client()
    client.connect("mqtt.eclipseprojects.io", 1883, 60)
    while True:
        message = input('Mensaje -> ')
        client.publish("sensor/uno", message)
        client.loop()