import pymssql

server = "192.168.2.197"
db_user = "sa"
db_password = "Duefelsiek1!"
database = "SWP"

filename_1 = "src\\setup\\alter_1.sql"
filename_2 = "src\\setup\\alter_2.sql"
try:
    file = open(filename_1, "r")
    querry_1 = file.read()
    file.close()
except OSError:
    print("Die Datei {filename_1} konnte nicht geöffnet werden.")
try:
    file = open(filename_2, "r")
    querry_2 = file.read()
    file.close()
except OSError:
    print("Die Datei {filename_1} konnte nicht geöffnet werden.")


connection = pymssql.connect(
    server=server, user=db_user, password=db_password, database=database
)
cursor = connection.cursor()
cursor.execute(querry_1)
connection.commit()
cursor.execute(querry_2)
connection.commit()
cursor.close()
connection.close()
