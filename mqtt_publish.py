import paho.mqtt.client as mqtt #import the client1
broker_address="test.mosquitto.org"
topic = "home/room"
client = mqtt.Client("P1") #create new instance
client.connect(broker_address,1883,60) #connect to broker
client.publish(topic,"test msg")#publish
client.disconnect()
