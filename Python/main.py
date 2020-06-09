
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
"""
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
"""

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
    ui.printconsole('Wollen sie Daten lesen [l], Daten schreiben [s] oder beenden [b]')
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
            pass
            #Welche Daten wollen sie schreiben?
            #hier nötigen Parameter abfragen
            #schreiben in DB
            #validierung wegen einfachheit sparen?
            #eventuell die Zeile abfragen um zu validieren, dass sie geschrieben wurde
        else:
            ui.printconsole('Diese Tabelle gibt es nicht.')

    if userinput == 'b':
        break
        #oder Beenden
        #Programm wird beendet
