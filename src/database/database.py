import pymssql
from data.comment import Comment
from data.game import Game
from data.genre import Genre
from data.picture import Picture
from data.publisher import Publisher
from data.review import Review
from data.user import User
from data.usk import Usk
from data.game_account import Game_account
from data.profile import Profile
from data.list import List
from routes.user import user_id

server = "192.168.178.67"
db_user = "sa"
db_password = "Duefelsiek1!"
database = "SWP"



def get_games(where_string, tuple):
    query_select_game = """SELECT ga.ID, ga.[NAME], ga.RELEASJAHR, ga.BESCHREIBUNG, ga.WEBSITE, ga.ERSTELLUNGSDATUM, pb.ID, pb.[NAME], pb.BESCHREIBUNG, pb.WEBSITE, pub_pic.ID, pub_pic.PFAD, pub_pic.ERSTELLUNGS_DATUM, pub_pic.AENDERUNGS_DATUM, usk.ID, usk.[NAME], usk_pic.ID, usk_pic.PFAD, usk_pic.ERSTELLUNGS_DATUM, usk_pic.AENDERUNGS_DATUM, gr.ID, gr.[NAME], gr.BESCHREIBUNG, gr.ERSTELLUNGSDATUM
FROM GAME ga
LEFT JOIN PUBLISHER pb ON ga.PUB_ID = pb.ID LEFT JOIN GENRE gr ON ga.GEN_ID = gr.ID LEFT JOIN USK usk ON ga.USK_ID = usk.ID LEFT JOIN BILD usk_pic ON usk.ID = usk_pic.USK_ID LEFT JOIN BILD pub_pic ON pb.ID = pub_pic.PUB_ID
WHERE """ +where_string
    query_select_pic = """SELECT ID, PFAD, PRIORITAET, ERSTELLUNGS_DATUM, AENDERUNGS_DATUM FROM BILD WHERE GAM_ID = %s ORDER BY PRIORITAET ASC"""
    con = pymssql.connect(
        server=server, user=db_user, password=db_password, database=database
    )
    cur = con.cursor()
    cur.execute(query_select_game,tuple)
    games = cur.fetchall()
    res = []
    for game in games:
        (
            id, name, release_year, description, website, creation_date,
            publisher_id, publisher_name, publisher_description, publisher_website, publisher_pic_id, publisher_pic_path, publisher_pic_creation_date, publisher_pic_change_date,
            usk_id, usk_name, usk_pic_id, usk_pic_path, usk_pic_creation_date, usk_pic_change_date,
            genre_id, gerne_name, genre_description, genre_creation_date,
        ) = game
        cur.execute(query_select_pic,id)
        pics = []
        for pic in cur:
            pics.append(Picture(*pic))
        res.append(
            Game(id, name, release_year, description, website, creation_date, None,
                Publisher(publisher_id, publisher_name, publisher_description, publisher_website,
                    Picture(publisher_pic_id, publisher_pic_path, 1, publisher_pic_creation_date, publisher_pic_change_date)
                ),
                Usk(usk_id, usk_name, None,
                    Picture( usk_pic_id, usk_pic_path, 1, usk_pic_creation_date, usk_pic_change_date),
                ),
                pics,
                Genre(genre_id, gerne_name, genre_description, genre_creation_date),
            )
        )
    cur.close()
    con.close()
    return res

def get_games_from_special_list(title):
    return get_games(""" ga.ID IN (SELECT gl.ID FROM LISTE li 
LEFT JOIN GAME_LIST gl ON li.ID = gl.LIS_ID
LEFT JOIN [USER] us ON li.USE_ID = us.ID
WHERE li.TITEL = %s AND us.E_MAIL = 'admin@gamescore.de')""",(title,))

def get_popular_games():
    return get_games_from_special_list("POPULAR_GAMES")

def get_new_game():
    return get_games_from_special_list("NEW_GAME")

def get_game_by_id(id):
    query_select = """SELECT REVIEW.ID, REVIEW.FREITEXT, CAST(REVIEW.RATING AS int), REVIEW.ZEI_ID, REVIEW.ERSTELLUNGS_DATUM, REVIEW.AENDERUNGSDATUM, REVIEW.GAM_ID, PROFIL.USE_ID FROM REVIEW JOIN PROFIL ON REVIEW.PRO_ID = PROFIL.ID WHERE GAM_ID = %s AND GELOSCHT = 0"""
    game = get_games("ga.ID = %s",(id,))[0]
    con = pymssql.connect(
        server=server, user=db_user, password=db_password, database=database
    )
    cur = con.cursor()
    cur.execute(query_select,(id,))
    for rev in cur:
        comment_id,text,rating,time_played_id,creation_date,change_date,game_id,user_id = rev
        game.add_review(Review(comment_id,text,rating,time_played_id,creation_date,change_date,False,game_id,user_id))
    cur.close()
    con.close()
    return game

def search_games(title,genre,release_year,publisher):
    where_clause = "ga.[name] LIKE %s"
    value_list = ["%"+title+"%"]
    if genre is not None:
        where_clause+= "AND gr.[NAME] LIKE %s"
        value_list.append("%"+genre+"%")
    if release_year is not None:
        where_clause+= "AND ga.RELEASJAHR LIKE %s"
        value_list.append(release_year)
    if publisher is not None:
        where_clause+= "AND pb.[NAME] LIKE %s"
        value_list.append("%"+publisher+"%")
    return get_games(where_clause,tuple(value_list))

def get_all_genres():
    query_select="SELECT ID, [NAME], BESCHREIBUNG, ERSTELLUNGSDATUM FROM GENRE"
    con = pymssql.connect(
        server=server, user=db_user, password=db_password, database=database
    )
    cur = con.cursor()
    cur.execute(query_select)
    res = []
    for gerne in cur:
        res.append(Genre(*gerne))
    cur.close()
    con.close()
    return res

def get_all_publisher():
    query_select="SELECT PUBLISHER.ID, PUBLISHER.[NAME], PUBLISHER.BESCHREIBUNG, PUBLISHER.WEBSITE, BILD.ID, BILD.PFAD, BILD.PRIORITAET, BILD.ERSTELLUNGS_DATUM, BILD.AENDERUNGS_DATUM FROM PUBLISHER LEFT JOIN BILD ON PUBLISHER.ID = BILD.PUB_ID"
    con = pymssql.connect(
        server=server, user=db_user, password=db_password, database=database
    )
    cur = con.cursor()
    cur.execute(query_select)
    res = []
    for pub in cur:
        id,name,description,website,pic_id,path,priority,creation_date,creation_date = pub
        res.append(Publisher(id,name,description,website,Picture(pic_id,path,priority,creation_date,creation_date)))
    cur.close()
    con.close()
    return res

def get_reviews_by_game_id(id):
    query_select_review = "SELECT rev.ID, rev.FREITEXT, CAST(rev.RATING AS INT), rev.ZEI_ID, rev.ERSTELLUNGS_DATUM, rev.AENDERUNGSDATUM, rev.GAM_ID, PROFIL.USE_ID FROM REVIEW rev JOIN PROFIL ON PROFIL.ID = rev.PRO_ID WHERE rev.GAM_ID = %s AND rev.GELOSCHT = 0"
    query_select_comments = "SELECT KOMMENTAR.ID, KOMMENTAR.FREITEXT, KOMMENTAR.ERSTELLUNGS_DATUM, KOMMENTAR.AENDERUNGS_DATUM, KOMMENTAR.GELOSCHT,'review',KOMMENTAR.REV_ID,NULL,PROFIL.USE_ID FROM KOMMENTAR JOIN PROFIL ON PROFIL.ID = KOMMENTAR.PRO_ID WHERE KOMMENTAR.REV_ID = %s"
    con = pymssql.connect(
        server=server, user=db_user, password=db_password, database=database
    )
    cur = con.cursor()
    cur.execute(query_select_review, (id,))
    reviews = cur.fetchall()
    res = []
    for review in reviews:
        comment_id,text,rating,time_played_id,creation_date,change_date,game_id,user_id = review
        rev = Review(comment_id,text,rating,time_played_id,creation_date,change_date,False,game_id,user_id)
        cur.execute(query_select_comments, (rev.get_id(),))
        for com in cur:
            rev.add_comments(Comment(*com))
        res.append(rev)
    cur.close()
    con.close()
    return res

def get_average_rating(id):
    query = "SELECT AVG(RATING)  FROM REVIEW WHERE GAM_ID = %s"
    con = pymssql.connect(
        server=server, user=db_user, password=db_password, database=database
    )
    cur = con.cursor()
    cur.execute(query, (id,))
    res = cur.fetchone()
    res, = res
    cur.close()
    con.close()
    return float(res)

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
