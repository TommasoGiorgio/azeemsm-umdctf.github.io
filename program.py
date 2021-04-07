import serial
import time
import requests

f=open("maker.key","r")
secret_key=f.read().strip()
my_data = { "value1" : "azeemsm.umdctf@gmail.com", "value2" : "Azeem" }

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
print("running...")

while True:
    try:
        data=arduino.readline()
        if data:
            message = data.decode('UTF-8').rstrip('\n')
            if "ring!" in message:
                #send request to webhooks so ifttt can do its thing!
                r=requests.post("https://maker.ifttt.com/trigger/ring/with/key/"+secret_key, data=my_data)
                print(r.text)
                
    except:
        arduino.close()
