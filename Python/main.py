from dbConnection import Database as db
from sqlalchemy import Table, Column, String, Integer, ForeignKey, DateTime
import userinterface as ui
from centertable import Ordertimes
from centertable import Centertable
from centertable import Customertable
from centertable import Producttable
from sqlalchemy.orm import class_mapper

database = db('postgres','Test','localhost',5432,'postgres')

dic={
    'Ordertimes': Ordertimes,
    'Centertable':Centertable,
    'Customertable':Customertable,
    'Producttable':Producttable
}

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

#order = Ordertimes(on_id= 'test',orderdate='2020-10-10 00:00:00',qtr_id=10,month_id=10,year_id=2020)

#database.create_object(order)

test = database.session.query(Ordertimes).filter(Ordertimes.year_id==2020)
for x in test:
    print(x)