import os
import time
import urllib3   #https://urllib3.readthedocs.io/en/latest/
http = urllib3.PoolManager()
KEY = "SA72C8CVDX16H3HB"
f1 = 50
f2 = 50
while True:
	try:
		baseURL = "https://api.thingspeak.com/update?api_key=%s" %(KEY)
		url = baseURL+"&field1=%f,&field2=%f" %(f1,f2)
		print(url)
		response = http.request('GET',url)
		print (response.data)
		time.sleep(1)
		f1 = f1 + 10
		f2 = f2 + 5
	except KeyboardInterrupt:
		print("Stopped")
		break
