#Azeem's Code
import serial
import time
import requests

#Read secret key from file for security!
f=open("maker.key","r")
secret_key=f.read().strip()

#Connect to arduino through serial (mine is on /dev/ttyUSB0 but this may change depending on which port I plug into)
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
print("running...")

#Never stop!!!
while True:
    try:
        #read from arduino
        data=arduino.readline()
        if data:
            #decode the data as UTF-8 (normal text) and remove new line
            message = data.decode('UTF-8').rstrip('\n')
            if "ring!" in message: #check if it says ring! (not sure what else it could be at the moment looking at the arduino code)
                #send request to webhooks so ifttt can do its thing!
                #send post request through ifttt webhook (this will send me email)
                r=requests.post("https://maker.ifttt.com/trigger/ring2/with/key/"+secret_key)
                print(r.text)
                
    except:
        #there was an error uh oh lets exit
        arduino.close()
        break
