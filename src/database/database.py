import pymssql
from data.game_account import Game_account
from data.profile import Profile
from data.user import User

server = "192.168.2.197"
db_user = "sa"
db_password = "Duefelsiek1!"
database = "SWP"


def login(e_mail, password):
    query_select = "SELECT us.id AS ANZAHL FROM [USER] us WHERE us.E_MAIL = %s AND us.PASSWORT = %s"
    query_update = "UPDATE PROFIL SET LOGIN_STATUS = 1 WHERE USE_ID = %s"
    con = pymssql.connect(server=server, user=db_user,
                          password=db_password, database=database)
    cur = con.cursor()
    cur.execute(query_select, (e_mail, password))
    res = cur.fetchone()
    if (res is not None):
        res, = res
    cur.execute(query_update, (res,))
    con.commit()
    cur.close()
    con.close()
    return res


def logout(id):
    query_update = "UPDATE PROFIL SET LOGIN_STATUS = 0 WHERE USE_ID = %s"
    con = pymssql.connect(server=server, user=db_user,
                          password=db_password, database=database)
    cur = con.cursor()
    cur.execute(query_update, (id,))
    con.commit()
    cur.close()
    con.close()


def create_user(user: User):
    query_mail = "SELECT COUNT(*) FROM [USER] WHERE E_MAIL = %s"
    query_user = "INSERT INTO [USER] (E_MAIL,PASSWORT,REGISTRIEUNGSDATUM, USERNAME) OUTPUT INSERTED.ID VALUES (%s,%s,%s,%s)"
    query_profile = "INSERT INTO PROFIL (LOGIN_STATUS, [NAME],use_id) VALUES (0,%s,%s)"
    con = pymssql.connect(server=server, user=db_user,
                          password=db_password, database=database)
    cur = con.cursor()
    cur.execute(query_mail, (user.get_e_mail(),))
    res, = cur.fetchone()
    if (res > 0):
        cur.close()
        con.close()
        return False
    cur.execute(query_user, (user.get_e_mail(), user.get_password(),
                user.get_register_date(), user.get_username()))
    res, = cur.fetchone()
    cur.execute(query_profile, (user.get_username(), res))
    con.commit()
    cur.close()
    con.close()
    return True


def get_user_by_id(id):
    query = "SELECT pr.LOGIN_STATUS, pr.[ALTER], pr.LAND, pr.[NAME], pr.BIO, NULL AS FAVORITE_GAME, sp.ID, sp.TYP, sp.AENDERDATUM FROM [USER] us LEFT JOIN PROFIL pr on us.ID = pr.USE_ID LEFT JOIN SPIELEACCOUNT sp on pr.ID = sp.PRO_ID WHERE us.ID = %s"
    con = pymssql.connect(server=server, user=db_user,
                          password=db_password, database=database)
    cur = con.cursor()
    cur.execute(query, (id,))
    row = cur.fetchone()
    profile = Profile(row[0], row[1], row[2], row[3], row[4], row[5])
    while row is not None:
        profile.add_game_account(Game_account(row[6], row[7], "", row[8]))
        row = cur.fetchone()
    cur.close()
    con.close()
    return profile


def get_user(id):
    query = """SELECT pr.LOGIN_STATUS, pr.[ALTER], pr.LAND, pr.[NAME], pr.BIO, NULL AS FAVORITE_GAME,
             sp.ID, sp.TYP, sp.AENDERDATUM,
             us.ID, us.USERNAME, us.E_MAIL, us.REGISTRIEUNGSDATUM
             FROM [USER] us LEFT JOIN PROFIL pr on us.ID = pr.USE_ID LEFT JOIN SPIELEACCOUNT sp on pr.ID = sp.PRO_ID WHERE us.ID = %s"""
    con = pymssql.connect(server=server, user=db_user,
                          password=db_password, database=database)
    cur = con.cursor()
    cur.execute(query, (id,))
    row = cur.fetchone()
    profile = Profile(row[0], row[1], row[2], row[3], row[4], row[5], user=User(
        row[9], row[10], row[11], "", row[12]))
    while row is not None:
        profile.add_game_account(Game_account(row[6], row[7], "", row[8]))
        row = cur.fetchone()
    cur.close()
    con.close()
    return profile

def update_user(profile):
    query = ""

def search_users(username):
    query = "select * from PROFIL where PROFIL.NAME like %s"
    con = pymssql.connect(server=server, user=db_user,
                          password=db_password, database=database)
    cur = con.cursor()
    cur.execute(query, (username,))
    profile_list = []
    for profile in cur:
        profile_list.append(Profile(profile[0], profile[1], profile[2], profile[3], profile[4], profile[5]))
    cur.close()
    con.close()
    return profile_list
