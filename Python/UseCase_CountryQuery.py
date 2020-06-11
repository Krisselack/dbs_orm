# Python script 
# File: UseCase_CountryQuery.py
# Contact: bran.chri@gmail.com
# Date:  7.06.2020
# Copyright (C) 2020
# Description:

# System-Setup 
import os
from sys import platform
if not"Python" in os.getcwd(): 
    os.chdir("./Python/") # damit die Module gefunden werden

# Import der notwendigen Module 
from dbConnection import Database as db
from sqlalchemy import Table, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import class_mapper
import userinterface as ui
from salesdb_declaration import Ordertimes, Centertable, Customertable, Producttable
from tkinter import *
import tkinter as tk
from sqlalchemy import inspect

# unterschiedliche Passwörter 
if platform == "linux": 
    database = db('postgres','postgres','localhost',5432,'postgres')
else:
    database = db('postgres','Test','localhost',5432,'postgres')

database.dbtest()

    # Tabellen 
dic={'Ordertimes': Ordertimes,
    'Centertable':Centertable,
    'Customertable':Customertable,
    'Producttable':Producttable
}

# Get data 
ct_fetch = database.session.query(Centertable).all()
pr_fetch = database.session.query(Producttable).all()
cu_fetch = database.session.query(Customertable).all()
ot_fetch = database.session.query(Ordertimes).all()


# Auslesen der einzelnen Daten 
ct_fetch[0].sales
pr_fetch[0].productline

# unique list of product types 
prod_types = []
for x in pr_fetch:
    if x.productline not in prod_types:
        prod_types.append(x.productline)
prod_types

# unique list of countries  
country_types = []
for x in cu_fetch:
    if x.country not in country_types:
        country_types.append(x.country)
country_types

# Auslesen der Customer-Spalten 
a = inspect(cu_fetch[0]) 
attr_names = [c_attr.key for c_attr in a.mapper.column_attrs]

# Dropdown-Beispiel von hier:  https://pythonspot.com/tk-dropdown-example/
# Erweiterung von hier: https://stackoverflow.com/questions/55750244/how-to-add-a-sequential-dropdown-menu-in-a-single-tkinter-window

root = Tk()
root.title("Tk dropdown country sales")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 200)

# Create a Tkinter variable
tkvar = StringVar(root)
tkvar2 = StringVar(root)
tkvar3 = StringVar(root)

# Dictionary with options
choices = country_types
choice2 = prod_types
choice3 = attr_names

tkvar.set('USA') # set the default option
tkvar2.set('Motorcycles') # set the default option
tkvar3.set('country') # set the default option

Label(mainframe, text="Choose a country and product type for sum of Sale \n (und unten die Ausgabe der Customertable nach Country (Konsolenprint))").grid(row = 1, column = 1)

popupMenu = tk.OptionMenu(mainframe, tkvar, *choices)
popupMenu.grid(row=2, column=1)

popupMenu2 = tk.OptionMenu(mainframe, tkvar2, *choice2)
popupMenu2.grid(row=3, column=1)  # ADDED

popupMenu3 = tk.OptionMenu(mainframe, tkvar3, *choice3)
popupMenu3.grid(row=4, column=1)  # ADDED

# on change dropdown value
def change_dropdown(*args):

    # ORM-Abfrage - Summe Sales
    mc_sales = database.session.query(Centertable).join(Customertable).join(Producttable).filter(Customertable.country == tkvar.get(), Producttable.productline == tkvar2.get()).all()

    col_name = tkvar3.get()
    print(col_name) 

    # ORM-Abfrage - Spalte Customertable nach Land 
    customerquery = database.session.query(getattr(Customertable,"{}".format(col_name))).filter(Customertable.country == tkvar.get()).all()
    print(customerquery)

    # für Summe Sales 
    mcsalessum = []
    for x in mc_sales:
        mcsalessum.append(x.sales)
    
    # Ausgabe 
    res = tk.StringVar(root, "Land: " + tkvar.get() + " Produkt: " + tkvar2.get() + " Summe: " + str(int(sum(mcsalessum))))  
        
    speak = tk.Message(root,
            textvariable = res,
            width=500)
    speak.pack()

# link function to change dropdown
tkvar.trace('w', change_dropdown)
tkvar2.trace('w', change_dropdown)
tkvar3.trace('w', change_dropdown)

root.mainloop()
