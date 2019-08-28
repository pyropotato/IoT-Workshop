import paho.mqtt.client as mqtt #import the client1
broker_address="test.mosquitto.org"
client = mqtt.Client("P1") #create new instance
client.connect(broker_address,1883,60) #connect to broker
client.publish("jack/tests","fuk u")#publish
client.disconnect()
