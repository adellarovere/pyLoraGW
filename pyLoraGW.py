import socket
import datetime
import time
import random

_TTNSERVER = "router.eu.thethings.network"
_TTNPORT = 1700


version = bytes([1])
#mac = bytes([0xDE, 0xAD, 0xBE, 0xFF, 0xFF, 0xFE, 0xFE, 0xED])
mac = bytes([0xDE, 0xAD, 0xBE, 0xEF, 0xCA, 0xFE, 0xFE, 0xED])



sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # 

while(1):
    status_report = version + bytes([random.randrange(255), random.randrange(255)]) + bytes([ 0x00 ]) + mac
    now = datetime.datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S CET")
    # JSON Payload
    Pld = r'{"stat":{ "time": "' + dt_string + r'", "lati":"0.0", "long":"0.0", "alti":"0", "rxnb":"0", "rxok":"0", "rxfw":"0", "ackr":"0", "dwnb":"0", "txnb":"0", "pfrm":"ESP8266", "mail":"foo@bar.net", "desc":"My Fake GW"}}'
    tx = status_report + str.encode(Pld) #+ bytes([0x00])

    sock.sendto(tx, (_TTNSERVER, _TTNPORT))

    time.sleep(30) #every 30 seconds
    print(tx)
    print(' ')


