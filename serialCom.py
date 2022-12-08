import serial, json
def serialCom():
    ser = serial.Serial('/dev/serial0',115200,timeout=1)
    #msg=json.dumps({"direction": 1, "switch": "true", "alarm": "false"})
    #print(msg)  
    #ser.write(str.encode(msg)) # write a string
    x=ser.readline()
    #loop=0
    print(x)
    jsonX=json.loads(x)
    #jsonX=json.loads(str(msg))
    #print(jsonX["switch"])
    ser.close()
    return jsonX
