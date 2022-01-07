
import pymssql
from data.game import Game
from data.genre import Genre
from data.picture import Picture
from data.publisher import Publisher
from data.user import User
from data.usk import Usk
from data.game_account import Game_account
from data.profile import Profile
from data.list import List

server = "192.168.2.197"
db_user = "sa"
db_password = "Duefelsiek1!"
database = "SWP"


def get_popular_games():
    query_select_game = """SELECT ga.ID, ga.[NAME], ga.RELEASJAHR, ga.BESCHREIBUNG, ga.WEBSITE, ga.ERSTELLUNGSDATUM, pb.ID, pb.[NAME], pb.BESCHREIBUNG, pb.WEBSITE, usk.ID, usk.[NAME], usk_pic.ID, usk_pic.PFAD, usk_pic.ERSTELLUNGS_DATUM, usk_pic.AENDERUNGS_DATUM, gr.ID, gr.[NAME], gr.BESCHREIBUNG, gr.ERSTELLUNGSDATUM
                    FROM GAME ga
LEFT JOIN PUBLISHER pb ON ga.PUB_ID = pb.ID LEFT JOIN GENRE gr on ga.GEN_ID = gr.ID LEFT JOIN USK usk on ga.USK_ID = usk.ID LEFT JOIN BILD usk_pic ON usk.ID = usk_pic.USK_ID 
WHERE ga.ID IN (SELECT gl.ID FROM LISTE li 
        LEFT JOIN GAME_LIST gl ON li.ID = gl.LIS_ID
        LEFT JOIN USER us ON li.USE_ID = us.ID
        WHERE li.TITEL = 'POPULAR_GAMES' AND us.E_MAIL = 'admin@gamescore.de')"""
    query_select_pic = """SELECT ID, PFAD, PRIORITAET, ERSTELLUNGS_DATUM, AENDERUNGS_DATUM FORM BILD WHERE GAM_ID = %s OREDR BY PRIORITAET ASC"""
    con = pymssql.connect(
        server=server, user=db_user, password=db_password, database=database
    )
    cur = con.cursor()
    cur.execute(query_select_game)
    res = []
    for game in cur:
        (
            id,
            name,
            release_year,
            description,
            website,
            creation_date,
            publisher_id,
            publisher_name,
            publisher_description,
            publisher_website,
            usk_id,
            usk_name,
            usk_pic_id,
            usk_pic_path,
            usk_pic_creation_date,
            usk_pic_change_date,
            genre_id,
            gerne_name,
            genre_description,
            genre_creation_date,
        ) = game
        cur_pic = con.cursor()
        cur_pic.execute(query_select_pic,id)
        pics = []
        for pic in cur_pic:
            pics.append(Picture(*pic))
        res.append(
            Game(
                id,
                name,
                release_year,
                description,
                website,
                creation_date,
                None,
                Publisher(
                    publisher_id,
                    publisher_name,
                    publisher_description,
                    publisher_website,
                ),
                Usk(
                    usk_id,
                    usk_name,
                    None,
                    Picture(
                        usk_pic_id,
                        usk_pic_path,
                        1,
                        usk_pic_creation_date,
                        usk_pic_change_date,
                    ),
                ),
                pics,
                Genre(genre_id, gerne_name, genre_description, genre_creation_date),
            )
        )
    cur.close()
    con.close()
    return res


def login(e_mail, password):
    query_select = "SELECT us.id AS ANZAHL FROM [USER] us WHERE us.E_MAIL = %s AND us.PASSWORT = %s"
    query_update = "UPDATE PROFIL SET LOGIN_STATUS = 1 WHERE USE_ID = %s"
    con = pymssql.connect(
        server=server, user=db_user, password=db_password, database=database
    )
    cur = con.cursor()
    cur.execute(query_select, (e_mail, password))
    res = cur.fetchone()
    if res is not None:
        (res,) = res
    cur.execute(query_update, (res,))
    con.commit()
    cur.close()
    con.close()
    return res


def logout(id):
    query_update = "UPDATE PROFIL SET LOGIN_STATUS = 0 WHERE USE_ID = %s"
    con = pymssql.connect(
        server=server, user=db_user, password=db_password, database=database
    )
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
        profile_list.append(
            Profile(profile[0], profile[1], profile[2], profile[3], profile[4], profile[5]))
    cur.close()
    con.close()
    return profile_list


def create_list(list: List, user_id):
    query = "INSERT INTO LISTE (TITEL, OEFFENTLICH, USE_ID) VALUES (%s,%s,%s)"
    con = pymssql.connect(server=server, user=db_user,
                          password=db_password, database=database)
    cur = con.cursor()
    cur.execute(query, (list.get_title(), list.get_public(), user_id))
    con.commit()
    cur.close()
    con.close()
    return True
