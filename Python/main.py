
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

# es sollten alle vom centertable zu den anderen 1:n sein 

while(True):
    ui.printconsole('Welche Tabelle wollen sie abfragen:')
    tabelle = ui.getinput()

    if (tabelle in dic):
        output = database.get_table(dic[tabelle])
        for x in output:
            ui.printconsole(x)
    else:
        ui.printconsole('Tabelle gibt es nicht')
    ui.printconsole('wollen sie beenden? x eingeben')
    if ui.getinput() == 'x':
        break


#hier müsste man immer den primarykey manuell angeben, denke mit int als pk wäre es einfacher
#hab zwar nicht genauer geschaut aber so nebenbei gelesen, dass es einen autoinc pk gibt
#hier mit string immer den höchsten auslesen und manuell eins raufzählen geht zwar, ist aber denke ich nciht optimal

# order = Ordertimes(on_id= 'test',orderdate='2020-10-10 00:00:00',qtr_id=10,month_id=10,year_id=2020)

# database.create_object(order)

# test = database.session.query(Ordertimes).filter(Ordertimes.year_id==2020) 
# for x in test:
#     print(x)



# Möglicher Usecase:
# sum sales of product and country -> country + product selector gui

# Get data 
ct_fetch = database.session.query(Centertable).all()
pr_fetch = database.session.query(Producttable).all()
cu_fetch = database.session.query(Customertable).all()
ot_fetch = database.session.query(Ordertimes).all()

# Auslesen der einzelnen Daten (-> Pandas-Analyse) 
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



# Verwenden der API zur Daten Abfrage:
# FILTER KANN MAN AUF Variable setzen 
mc_sales_in_USA = database.session.query(Centertable) \
    .join(Customertable) \
    .join(Producttable) \ 
    .filter(Customertable.country == 'USA', Producttable.productline == 'Motorcycles') \
    .all()

ussales = []
for x in mc_sales_in_USA:
    ussales.append(x.sales)

sum(ussales)


# Beispiel von hier:  https://pythonspot.com/tk-dropdown-example/
from tkinter import *
import tkinter as tk
# from tk import *

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

# Dictionary with options
choices = country_types
tkvar.set('USA') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a country for Motorcycle Sale").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    # print( tkvar.get() )

    mc_sales = database.session.query(Centertable) \
    .join(Customertable) \
    .join(Producttable) \ 
    .filter(Customertable.country == tkvar.get(), Producttable.productline == 'Motorcycles') \
    .all()

    mcsalessum = []
    for x in mc_sales:
        mcsalessum.append(x.sales)

    print(sum(mcsalessum))

# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()

 
