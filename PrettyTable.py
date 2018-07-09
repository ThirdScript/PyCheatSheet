#!/usr/bin/python

# Import The Main PrettyTable Function
from prettytable import PrettyTable

# Make A PrettyTable Object
chart = PrettyTable()

# Row By Row Method
# Set The Main Field Names
chart.set_field_names(["Name", "Age", "Lang"])
# Add Every Value IN Sertain Field
chart.add_row(["Space", "18", "Python"])
chart.add_row(["Joker", "21", "VB.NET"])
chart.add_row(["PRS", "24", "Ruby"])
chart.add_row(["Snape", "27", "PHP"])

# Column By Column Method
# Make A Field And Put Values Under
chart.add_column("Name",["Space","Joker","PRS","Snape"])
chart.add_column("Age",["18","21","24","28"])
chart.add_column("Lang",["Python","VB.NET","Ruby","PHP"])

# Delete A Single Row From The Table
# IN This Case [Space, 18, Python] Will Gone !
chart.del_row(0)

# Delete Every Data IN The Table But Keep The Field Names
# To Clear Everything And Set Other Values
chart.clear_rows()

print chart