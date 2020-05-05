import socket
import sys
import json



Host, PORT = "localhost", 3001
s = socket.socket()
s.connect((Host, PORT))
data={"matricules": ["18185", "17245"],"port": 1234,"name": "girls"}

msg = json.dumps(data).encode('utf8')
total = 0
while total < len(msg):
	sent = s.send(msg[total:])
	total += sent