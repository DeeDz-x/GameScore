SET IDENTITY_INSERT [USER] ON
INSERT INTO [USER] (ID,E_MAIL,PASSWORT, USERNAME) VALUES (0,'admin@gamescore.de','admin','admin')
SET IDENTITY_INSERT [USER] OFF
INSERT INTO PROFIL (LOGIN_STATUS, [NAME],use_id) VALUES (0,'admin',0)
INSERT INTO LISTE (TITEL, OEFFENTLICH, USE_ID) VALUES ('POPULAR_GAMES',0,0)
INSERT INTO LISTE (TITEL, OEFFENTLICH, USE_ID) VALUES ('NEW_GAME',0,0)
SET IDENTITY_INSERT GAME_LIST ON
INSERT INTO GAME_LIST (LIS_ID, ID) SELECT ID,1 FROM LISTE WHERE TITEL = 'POPULAR_GAMES'
INSERT INTO GAME_LIST (LIS_ID, ID) SELECT ID,2 FROM LISTE WHERE TITEL = 'POPULAR_GAMES'
INSERT INTO GAME_LIST (LIS_ID, ID) SELECT ID,3 FROM LISTE WHERE TITEL = 'POPULAR_GAMES'
INSERT INTO GAME_LIST (LIS_ID, ID) SELECT ID,4 FROM LISTE WHERE TITEL = 'POPULAR_GAMES'
INSERT INTO GAME_LIST (LIS_ID, ID) SELECT ID,5 FROM LISTE WHERE TITEL = 'POPULAR_GAMES'
INSERT INTO GAME_LIST (LIS_ID, ID) SELECT ID,6 FROM LISTE WHERE TITEL = 'NEW_GAME'
INSERT INTO GAME_LIST (LIS_ID, ID) SELECT ID,7 FROM LISTE WHERE TITEL = 'NEW_GAME'
INSERT INTO GAME_LIST (LIS_ID, ID) SELECT ID,8 FROM LISTE WHERE TITEL = 'NEW_GAME'
INSERT INTO GAME_LIST (LIS_ID, ID) SELECT ID,9 FROM LISTE WHERE TITEL = 'NEW_GAME'
INSERT INTO GAME_LIST (LIS_ID, ID) SELECT ID,10 FROM LISTE WHERE TITEL = 'NEW_GAME'
SET IDENTITY_INSERT GAME_LIST OFF

INSERT INTO BILD (USK_ID,PFAD,PRIORITAET) VALUES (1,'usk_0.png',1)
INSERT INTO BILD (USK_ID,PFAD,PRIORITAET) VALUES (2,'usk_6.png',1)
INSERT INTO BILD (USK_ID,PFAD,PRIORITAET) VALUES (3,'usk_12.png',1)
INSERT INTO BILD (USK_ID,PFAD,PRIORITAET) VALUES (4,'usk_16.png',1)
INSERT INTO BILD (USK_ID,PFAD,PRIORITAET) VALUES (5,'usk_18.png',1)
INSERT INTO BILD (PRO_ID,PFAD,PRIORITAET) SELECT ID,'placeholder_profile.png',1 FROM PROFIL
INSERT INTO BILD (GAM_ID,PFAD,PRIORITAET) SELECT ID,'placeholder_game_1.png',1 FROM GAME
INSERT INTO BILD (GAM_ID,PFAD,PRIORITAET) SELECT ID,'placeholder_game_2.png',2 FROM GAME
INSERT INTO BILD (GAM_ID,PFAD,PRIORITAET) SELECT ID,'placeholder_game_3.png',3 FROM GAME
INSERT INTO BILD (PUB_ID,PFAD,PRIORITAET) SELECT ID,'placeholder_pub.png',1 FROM PUBLISHER
