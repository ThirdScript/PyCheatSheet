#!/usr/bin/python

import socket
import sys

# ================================== Basic IO ===========================================
# TCP Socket Creation
tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Open Port "8000" ON Local Machine
# 2 Brackets Are Because The BIND() Input IS A Tuple
tsock.bind(("0.0.0.0", 8000))
# Accept Connection's And Listen ON Binded Port With Maximum 3 Client Handling
tsock.listen(3)
# Pass A Tuple That Include Client Handler , And IP + Port
(client, (_ip, _port)) = tsock.accept()
# Now We Send Data From The Socket To Client
client.send("Welcome To Space Server\n")
client.send("Server IS UP !\n")
# We Get User INPUT With 2048B Size Of Buffer And Pass IT INTO Data Variable
client.send("Name :: ")
_data = client.recv(2048)
# =============================== Echo Server ==========================================
# TCP Socket Creation
tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Open Port "8000" ON Local Machine
# 2 Brackets Are Because The BIND() Input IS A Tuple
tsock.bind(("0.0.0.0", 8000))
# Accept Connection's And Listen ON Binded Port With Maximum 3 Client Handling
tsock.listen(3)
# Pass A Tuple That Include Client Handler , And IP + Port
(client, (_ip, _port)) = tsock.accept()
# See User's IN The Server ....
print "[%s] Connected ......" %_ip
# Send A Welcom Message To Client
client.send("Welcom To Echo Server")
# We Define _Data Var And Put Something IN It ...
_data = "LoL"
# Till The User Didn't Hit Enter
while _data != '\n':
	# Get 2048B Data From Client
	_data = client.recv(2048)
	print "Client Sent [%s]" %_data
	client.send(_data)
# Close Client Side Connection ...
print "Closing The Connection ...."
client.close()
# Close The Hole TCP Connection
print "Shuting Down The Server"
tcpsock.close()
# ======================== Re-Active PORT ==============================
# IF The Connection Crash And Close IN A Bad Way !
# There IS A Option To Fix It For Ever !!!!
# Place This Code Under Socket Defnition
tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ====================== Client Side Socket =============================
# Same Shit Diffrent Day ....
tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Connect To Target [INPUT Of The Function IS A Tuple]
tsock.connect((_ip, _port))

# Infinit Loop For Connection
while True:
	_data = raw_input("Send :: ")
	tsock.send(_data)
	tsock.recv(2048)

tsock.close()