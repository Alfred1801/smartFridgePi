import serial, json
def serialCom():
    loop=1
    ser = serial.Serial('/dev/serial0',115200,timeout=1)
    msg=json.dumps({"direction": 0, "switch": "false", "alarm": "false"})
    #print(msg)  
    #ser.write(str.encode(msg)) # write a string
    #x=ser.readline()
    #loop=0
    #jsonX=json.loads(str(x))
    jsonX=json.loads(str(msg))
    print(jsonX["switch"])
    ser.close()
    return jsonX
