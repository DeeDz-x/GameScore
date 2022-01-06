from click.decorators import pass_obj
import pymssql

server="192.168.178.64"
user="sa"
db_password="Duefelsiek1!"
database = "SWP"


def login(e_mail,password):
    query_select = "SELECT us.id AS ANZAHL FROM [USER] us WHERE us.E_MAIL = %s AND us.PASSWORT = %s"
    query_update = "UPDATE PROFIL SET LOGIN_STATUS = 1 WHERE USE_ID = %s"
    con = pymssql.connect(server=server, user=user, password=db_password,database = database)
    cur = con.cursor()
    cur.execute(query_select,(e_mail,password))
    res = cur.fetchone()
    if (res is not None):
        res, = res
    cur.execute(query_update,(res,))
    cur.close()
    con.close()
    return res

def logout(id):
    query_update = "UPDATE PROFIL SET LOGIN_STATUS = 1 WHERE USE_ID = %s"
    con = pymssql.connect(server=server, user=user, password=db_password,database = database)
    cur = con.cursor()
    cur.execute(query_update,(id,))
    cur.close()
    con.close()