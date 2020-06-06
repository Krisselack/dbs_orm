from dbConnection import Database as db
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


