#!/usr/bin/python

# Import Most Used Objects
from tinydb import TinyDB, Query

# Make A TinyDB Object And Connect IT To ./db.json
DB = TinyDB('db.json')

# Every Time For Inserting Data, TinyDB Will Get A Dictonary
DB.insert({"Name":"Space", "Age":18})
DB.insert({"Name":"PRS", "Age":24})

# To See Database Objects U Can Open "db.json" File
# Or Use This Command
DB.all()

# Thers A Tool For Searching Inside Database Called "Query"
# We Make A Query Object
Q = Query()

# Now We Can Search Inside Database And Find Matching Objects
# IN Searcg There Should Be A Boolean Output Of Your Statement
DB.search(Q['Name'] == "Space")

# To Update The Value OF A Variable IN The Database
# First Arg Get The New Values To Insert
# Second Arg Get The Object To Update
DB.update({"Name":"Sepehr"}, Q.Name == "Space")

# To Remove A Var Use This Kind OF Syntax
DB.remove(Q['Name'] == "Sepehr")
DB.remove(Q['Age'] < 18)

# To Trash Every Data IN The Database
DB.purge()

# Another Way To Use Querys
from tinydb import where
# DB.search(Q.['Name'] == "Space")
DB.search(where("Name") == "Space")

# Check And See IF A Value Exist Or Not
DB.search(Q["Name"].exists()) #True

# Using AND To Get The Best Output
DB.search(Q["Age"] == 24 & Q["Name"] == "PRS")

# Using OR Like &
DB.search(Q["Age"] == 24 | Q["Name"] == "PRS")

# Multiple Values IN One Line OF Inserting
# Get A List With Two Dictonarys IN It !
DB.insert_multiple([{'Name': 'John', 'Age': 22}, {'Name': 'John', 'Age': 37}])

