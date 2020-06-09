
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


# Möglicher Usecase:
# sum sales of product and country -> country + product selector gui

# Verwenden der API zur Daten Abfrage:
# FILTER KANN MAN AUF Variable setzen
"""
mc_sales_in_USA = database.session.query(Centertable) \
    .join(Customertable) \
    .join(Producttable) \ 
    .filter(Customertable.country == 'USA', Producttable.productline == 'Motorcycles') \
    .all()

ussales = []
for x in mc_sales_in_USA:
    ussales.append(x.sales)

sum(ussales)
"""

# Ablauf für UseCase
while(True):
    #1 Wollen sie Daten lesen
    ui.printconsole('Wollen sie Daten lesen [l], Daten schreiben [s], Daten updaten [u] oder beenden [b]')
    userinput = ui.getinput()

    if userinput == 'l':
        #Daten lesen
        ui.printconsole('Welches Land möchten sie abfragen?')
        countries = []
        [countries.append(x[0]) for x in database.session.query(Customertable.country).distinct()]
        print(countries)
        country = ui.getinput()

        if country in countries:
            countrysales = []
            [countrysales.append(x.sales) for x in database.session.query(Centertable).join(Customertable).join(Producttable).filter(Customertable.country == country).all()]
            # Abgefragte daten ausgeben
            ui.printconsole(sum(countrysales))

        else:
            ui.printconsole('Dieses Land gibt es nicht in der Tabelle')


    if userinput == 's':
        ui.printconsole('Welche Tabelle möchten sie schreiben?')
        # Tabellen abfragen
        table = ui.getinput()
        if table in dic:
            #oder Schreiben
            if table == 'Producttable':
                #hier nötigen Parameter abfragen
                ui.printconsole('ID char5')
                id = ui.getinput()
                ui.printconsole('msrp int')
                msrp = ui.getinput()
                ui.printconsole('productline char20')
                productline = ui.getinput()
                ui.printconsole('productcode char20')
                productcode = ui.getinput()
                #schreiben in DB
                product = Producttable(pr_id=id, msrp=msrp, productline=productline, productcode=productcode)
                database.create_object(product)
                #die Zeile abfragen um zu validieren, dass sie geschrieben wurde
                test = database.session.query(Producttable).filter(Producttable.pr_id==id, Producttable.msrp==msrp, Producttable.productline==productline)
                for x in test:
                     print('pr_id: '+ x.pr_id +'| msrp: '+ str(x.msrp)+'| productline: ' + x.productline+'| productcode: ' + x.productcode)
        else:
            ui.printconsole('Diese Tabelle gibt es nicht.')

    if userinput =='u':
        customer = database.session.query(Customertable).get('CU1')
        print('cu_id: ' + customer.cu_id + '| customername: ' + customer.customername)
        ui.printconsole('customername char50')
        newname = ui.getinput()
        customer.customername = newname
        database.session.commit()
        database.session.refresh(customer)
        #customer = database.session.query(Customertable).get('CU1')
        print('cu_id: ' + customer.cu_id + '| customername: ' + customer.customername)
    if userinput == 'b':
        break
        #Programm wird beendet
