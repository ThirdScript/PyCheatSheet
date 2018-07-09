#!/usr/bin/python

# LIB
import pymongo

# First You Should Start The MongoDB Server
# There Will Be AN IP And A Port To Connect

# Base URL Will Be "mongodb://<IP>:<PORT>"
_base = "mongodb://127.0.0.1:27017"

# Connection Comes With "MongoClient" Function !
mongodb = pymongo.MongoClient(_base)

# After The Connection All The Internal Database Objects Will Be Usable Az List Objects
# So For Using A Database Inside The MongoDB Server Put The Name OF IT Inside ["DB_NAME"]
db = mongodb["Database"]

# To Get Into A Collection From The Database
# Use The Same Shit
cli = db["Company"]

# Now Tou Have A Simple MongoDB Shell From Python
# All MongoDB Commands Are Usable After .
_all_objects = cli.find({})
# Note :: This Will Return A Usable Object !
#  // :: Not Simple Stream Return

# Now We Can Print Out The Data
for i in _all_objects:
	print "<-- {} -->".format(i)

# Also There IS A Way To Make A List Out Of MongoDB Responses
_all_objects = cli.find({})
_objects = []
for local in _all_objects:
	_objects.append(local)
# Now _objects Has All The Search Result :D

