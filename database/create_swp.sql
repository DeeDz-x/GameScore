/*==============================================================*/
/* DBMS name:      Microsoft SQL Server 2017                    */
/* Created on:     09.12.2021 14:10:40                          */
/*==============================================================*/


if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('BEWERTUNG') and o.name = 'FK_BEWERTUN_BEWERTUNG_REVIEW')
alter table BEWERTUNG
   drop constraint FK_BEWERTUN_BEWERTUNG_REVIEW
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('BEWERTUNG') and o.name = 'FK_BEWERTUN_BEWERTUNG_PROFIL')
alter table BEWERTUNG
   drop constraint FK_BEWERTUN_BEWERTUNG_PROFIL
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('BILD') and o.name = 'FK_BILD_GAME_PICT_GAME')
alter table BILD
   drop constraint FK_BILD_GAME_PICT_GAME
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('BILD') and o.name = 'FK_BILD_PROFIL_PI_PROFIL')
alter table BILD
   drop constraint FK_BILD_PROFIL_PI_PROFIL
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('BILD') and o.name = 'FK_BILD_USK_PICTU_USK')
alter table BILD
   drop constraint FK_BILD_USK_PICTU_USK
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('GAME') and o.name = 'FK_GAME_GAME_GAME_GAME')
alter table GAME
   drop constraint FK_GAME_GAME_GAME_GAME
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('GAME') and o.name = 'FK_GAME_GENRE_GAM_GENRE')
alter table GAME
   drop constraint FK_GAME_GENRE_GAM_GENRE
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('GAME') and o.name = 'FK_GAME_PUBLISHER_PUBLISHE')
alter table GAME
   drop constraint FK_GAME_PUBLISHER_PUBLISHE
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('GAME') and o.name = 'FK_GAME_USK_GAME_USK')
alter table GAME
   drop constraint FK_GAME_USK_GAME_USK
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('GAME_LIST') and o.name = 'FK_GAME_LIS_GEHÖRT_GAME')
alter table GAME_LIST
   drop constraint FK_GAME_LIS_GEHÖRT_GAME
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('GAME_LIST') and o.name = 'FK_GAME_LIS_GEHÖRT_LISTE')
alter table GAME_LIST
   drop constraint FK_GAME_LIS_GEHÖRT_LISTE
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('KOMMENTAR') and o.name = 'FK_KOMMENTA_COMMENT_C_KOMMENTA')
alter table KOMMENTAR
   drop constraint FK_KOMMENTA_COMMENT_C_KOMMENTA
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('KOMMENTAR') and o.name = 'FK_KOMMENTA_KOMMENTAR_PROFIL')
alter table KOMMENTAR
   drop constraint FK_KOMMENTA_KOMMENTAR_PROFIL
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('KOMMENTAR') and o.name = 'FK_KOMMENTA_REVIEW_CO_REVIEW')
alter table KOMMENTAR
   drop constraint FK_KOMMENTA_REVIEW_CO_REVIEW
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('LISTE') and o.name = 'FK_LISTE_LIST_USER_USER')
alter table LISTE
   drop constraint FK_LISTE_LIST_USER_USER
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('NOTIFICATION') and o.name = 'FK_NOTIFICA_PROFIL_NO_PROFIL')
alter table NOTIFICATION
   drop constraint FK_NOTIFICA_PROFIL_NO_PROFIL
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('PROFIL') and o.name = 'FK_PROFIL_GEHÖRT_USER')
alter table PROFIL
   drop constraint FK_PROFIL_GEHÖRT_USER
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('REVIEW') and o.name = 'FK_REVIEW_REVIEW_GA_GAME')
alter table REVIEW
   drop constraint FK_REVIEW_REVIEW_GA_GAME
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('REVIEW') and o.name = 'FK_REVIEW_REVIEW_PR_PROFIL')
alter table REVIEW
   drop constraint FK_REVIEW_REVIEW_PR_PROFIL
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('REVIEW') and o.name = 'FK_REVIEW_REVIEW_TI_ZEITSTAF')
alter table REVIEW
   drop constraint FK_REVIEW_REVIEW_TI_ZEITSTAF
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('SPIELEACCOUNT') and o.name = 'FK_SPIELEAC_PROFIL_AC_PROFIL')
alter table SPIELEACCOUNT
   drop constraint FK_SPIELEAC_PROFIL_AC_PROFIL
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('"USER"') and o.name = 'FK_USER_GEHÖRT_PROFIL')
alter table "USER"
   drop constraint FK_USER_GEHÖRT_PROFIL
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('BEWERTUNG')
            and   name  = 'BEWERTUNG_USER_FK'
            and   indid > 0
            and   indid < 255)
   drop index BEWERTUNG.BEWERTUNG_USER_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('BEWERTUNG')
            and   name  = 'BEWERTUNG_REVIEW_FK'
            and   indid > 0
            and   indid < 255)
   drop index BEWERTUNG.BEWERTUNG_REVIEW_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('BEWERTUNG')
            and   type = 'U')
   drop table BEWERTUNG
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('BILD')
            and   name  = 'USK_PICTURE_FK'
            and   indid > 0
            and   indid < 255)
   drop index BILD.USK_PICTURE_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('BILD')
            and   name  = 'GEHORT_FK'
            and   indid > 0
            and   indid < 255)
   drop index BILD.GEHORT_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('BILD')
            and   name  = 'GAME_PICTURE_FK'
            and   indid > 0
            and   indid < 255)
   drop index BILD.GAME_PICTURE_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('BILD')
            and   type = 'U')
   drop table BILD
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('GAME')
            and   name  = 'PUBLISHER_GAME_FK'
            and   indid > 0
            and   indid < 255)
   drop index GAME.PUBLISHER_GAME_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('GAME')
            and   name  = 'GENRE_GAME_FK'
            and   indid > 0
            and   indid < 255)
   drop index GAME.GENRE_GAME_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('GAME')
            and   name  = 'GAME_GAME_FK'
            and   indid > 0
            and   indid < 255)
   drop index GAME.GAME_GAME_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('GAME')
            and   name  = 'USK_GAME_FK'
            and   indid > 0
            and   indid < 255)
   drop index GAME.USK_GAME_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('GAME')
            and   type = 'U')
   drop table GAME
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('GAME_LIST')
            and   name  = 'GEHORT_FK2'
            and   indid > 0
            and   indid < 255)
   drop index GAME_LIST.GEHORT_FK2
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('GAME_LIST')
            and   name  = 'GEHORT_FK'
            and   indid > 0
            and   indid < 255)
   drop index GAME_LIST.GEHORT_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('GAME_LIST')
            and   type = 'U')
   drop table GAME_LIST
go

if exists (select 1
            from  sysobjects
           where  id = object_id('GENRE')
            and   type = 'U')
   drop table GENRE
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('KOMMENTAR')
            and   name  = 'KOMMENTAR_PROFIL_FK'
            and   indid > 0
            and   indid < 255)
   drop index KOMMENTAR.KOMMENTAR_PROFIL_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('KOMMENTAR')
            and   name  = 'COMMENT_COMMENT_FK'
            and   indid > 0
            and   indid < 255)
   drop index KOMMENTAR.COMMENT_COMMENT_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('KOMMENTAR')
            and   name  = 'REVIEW_COMMENT_FK'
            and   indid > 0
            and   indid < 255)
   drop index KOMMENTAR.REVIEW_COMMENT_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('KOMMENTAR')
            and   type = 'U')
   drop table KOMMENTAR
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('LISTE')
            and   name  = 'LIST_USER_FK'
            and   indid > 0
            and   indid < 255)
   drop index LISTE.LIST_USER_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('LISTE')
            and   type = 'U')
   drop table LISTE
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('NOTIFICATION')
            and   name  = 'PROFIL_NOTIFICATION_FK'
            and   indid > 0
            and   indid < 255)
   drop index NOTIFICATION.PROFIL_NOTIFICATION_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('NOTIFICATION')
            and   type = 'U')
   drop table NOTIFICATION
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('PROFIL')
            and   name  = 'GEHORT_FK'
            and   indid > 0
            and   indid < 255)
   drop index PROFIL.GEHORT_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('PROFIL')
            and   type = 'U')
   drop table PROFIL
go

if exists (select 1
            from  sysobjects
           where  id = object_id('PUBLISHER')
            and   type = 'U')
   drop table PUBLISHER
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('REVIEW')
            and   name  = 'REVIEW_PROFIL_FK'
            and   indid > 0
            and   indid < 255)
   drop index REVIEW.REVIEW_PROFIL_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('REVIEW')
            and   name  = 'REVIEW_TIMESCALE_FK'
            and   indid > 0
            and   indid < 255)
   drop index REVIEW.REVIEW_TIMESCALE_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('REVIEW')
            and   name  = 'REVIEW_GAME_FK'
            and   indid > 0
            and   indid < 255)
   drop index REVIEW.REVIEW_GAME_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('REVIEW')
            and   type = 'U')
   drop table REVIEW
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('SPIELEACCOUNT')
            and   name  = 'PROFIL_ACCOUNT_FK'
            and   indid > 0
            and   indid < 255)
   drop index SPIELEACCOUNT.PROFIL_ACCOUNT_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('SPIELEACCOUNT')
            and   type = 'U')
   drop table SPIELEACCOUNT
go

if exists (select 1
            from  sysobjects
           where  id = object_id('SPIELE_RATING')
            and   type = 'U')
   drop table SPIELE_RATING
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('"USER"')
            and   name  = 'GEHORT_FK'
            and   indid > 0
            and   indid < 255)
   drop index "USER".GEHORT_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('"USER"')
            and   type = 'U')
   drop table "USER"
go

if exists (select 1
            from  sysobjects
           where  id = object_id('USK')
            and   type = 'U')
   drop table USK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('ZEITSTAFFEL')
            and   type = 'U')
   drop table ZEITSTAFFEL
go

if exists(select 1 from systypes where name='ACCOUNTTYP')
   execute sp_unbindrule ACCOUNTTYP
go

if exists(select 1 from systypes where name='ACCOUNTTYP')
   drop type ACCOUNTTYP
go

if exists(select 1 from systypes where name='BEWERTUNGSWERT')
   execute sp_unbindrule BEWERTUNGSWERT
go

if exists(select 1 from systypes where name='BEWERTUNGSWERT')
   drop type BEWERTUNGSWERT
go

if exists(select 1 from systypes where name='NOTIFICATIONTYPE')
   drop type NOTIFICATIONTYPE
go

if exists (select 1 from sysobjects where id=object_id('R_ACCOUNTTYP') and type='R')
   drop rule  R_ACCOUNTTYP
go

if exists (select 1 from sysobjects where id=object_id('R_BEWERTUNGSWERT') and type='R')
   drop rule  R_BEWERTUNGSWERT
go

create rule R_ACCOUNTTYP as
      @column in ('Steam','Origin','Playstation','Xbox')
go

create rule R_BEWERTUNGSWERT as
      @column in ('Gut','Schlect')
go

/*==============================================================*/
/* Domain: ACCOUNTTYP                                           */
/*==============================================================*/
create type ACCOUNTTYP
   from varchar(1024) not null
go

execute sp_bindrule R_ACCOUNTTYP, ACCOUNTTYP
go

/*==============================================================*/
/* Domain: BEWERTUNGSWERT                                       */
/*==============================================================*/
create type BEWERTUNGSWERT
   from varchar(1024) not null
go

execute sp_bindrule R_BEWERTUNGSWERT, BEWERTUNGSWERT
go

/*==============================================================*/
/* Domain: NOTIFICATIONTYPE                                     */
/*==============================================================*/
create type NOTIFICATIONTYPE
   from varchar(10)
go

/*==============================================================*/
/* Table: BEWERTUNG                                             */
/*==============================================================*/
create table BEWERTUNG (
   ID                   int                  not null,
   PRO_ID               int                  not null,
   REV_ID               int                  not null,
   WERT                 BEWERTUNGSWERT       not null,
   ERSTELLUNGSDATUM     datetime             not null default GETDATE(),
   AENDERUNGSDATUM      datetime             null,
   constraint PK_BEWERTUNG primary key (ID)
)
go

/*==============================================================*/
/* Index: BEWERTUNG_REVIEW_FK                                   */
/*==============================================================*/




create nonclustered index BEWERTUNG_REVIEW_FK on BEWERTUNG (REV_ID ASC)
go

/*==============================================================*/
/* Index: BEWERTUNG_USER_FK                                     */
/*==============================================================*/




create nonclustered index BEWERTUNG_USER_FK on BEWERTUNG (PRO_ID ASC)
go

/*==============================================================*/
/* Table: BILD                                                  */
/*==============================================================*/
create table BILD (
   ID                   int                  not null,
   USK_ID               int                  null,
   GAM_ID               int                  null,
   PRO_ID               int                  null,
   PFAD                 varchar(1024)        not null,
   PRIORITAET           int                  not null,
   ERSTELLUNGS_DATUM    datetime             null default GETDATE(),
   AENDERUNGS_DATUM     datetime             null,
   constraint PK_BILD primary key (ID)
)
go

/*==============================================================*/
/* Index: GAME_PICTURE_FK                                       */
/*==============================================================*/




create nonclustered index GAME_PICTURE_FK on BILD (GAM_ID ASC)
go

/*==============================================================*/
/* Index: GEHORT_FK                                             */
/*==============================================================*/




create nonclustered index GEHORT_FK on BILD (PRO_ID ASC)
go

/*==============================================================*/
/* Index: USK_PICTURE_FK                                        */
/*==============================================================*/




create nonclustered index USK_PICTURE_FK on BILD
go

/*==============================================================*/
/* Table: GAME                                                  */
/*==============================================================*/
create table GAME (
   ID                   int                  not null,
   GAM_ID               int                  null,
   GEN_ID               int                  not null,
   USK_ID               int                  not null,
   PUB_ID               int                  not null,
   NAME                 varchar(100)         not null,
   RELEASJAHR           varchar(10)          null,
   BESCHREIBUNG         varchar(1024)        null,
   PLATFORM             varchar(1024)        null,
   WEBSITE              varchar(100)         null,
   ERSTELLUNGSDATUM     datetime             null default GETDATE(),
   constraint PK_GAME primary key (ID)
)
go

/*==============================================================*/
/* Index: USK_GAME_FK                                           */
/*==============================================================*/




create nonclustered index USK_GAME_FK on GAME (USK_ID ASC)
go

/*==============================================================*/
/* Index: GAME_GAME_FK                                          */
/*==============================================================*/




create nonclustered index GAME_GAME_FK on GAME (GAM_ID ASC)
go

/*==============================================================*/
/* Index: GENRE_GAME_FK                                         */
/*==============================================================*/




create nonclustered index GENRE_GAME_FK on GAME (GEN_ID ASC)
go

/*==============================================================*/
/* Index: PUBLISHER_GAME_FK                                     */
/*==============================================================*/




create nonclustered index PUBLISHER_GAME_FK on GAME (PUB_ID ASC)
go

/*==============================================================*/
/* Table: GAME_LIST                                             */
/*==============================================================*/
create table GAME_LIST (
   ID                   int                  not null,
   GAM_ID               int                  not null,
   constraint PK_GAME_LIST primary key (ID, GAM_ID)
)
go

/*==============================================================*/
/* Index: GEHORT_FK                                             */
/*==============================================================*/




create nonclustered index GEHORT_FK on GAME_LIST (ID ASC)
go

/*==============================================================*/
/* Index: GEHORT_FK2                                            */
/*==============================================================*/




create nonclustered index GEHORT_FK2 on GAME_LIST (GAM_ID ASC)
go

/*==============================================================*/
/* Table: GENRE                                                 */
/*==============================================================*/
create table GENRE (
   ID                   int                  not null,
   NAME                 varchar(100)         not null,
   BESCHREIBUNG         varchar(1024)        null,
   ERSTELLUNGSDATUM     datetime             null default GETDATE(),
   constraint PK_GENRE primary key (ID)
)
go

/*==============================================================*/
/* Table: KOMMENTAR                                             */
/*==============================================================*/
create table KOMMENTAR (
   ID                   int                  not null,
   REV_ID               int                  not null,
   KOM_ID               int                  null,
   PRO_ID               int                  not null,
   FREITEXT             varchar(1024)        not null,
   ERSTELLUNGS_DATUM    datetime             null default GETDATE(),
   AENDERUNGS_DATUM     datetime             null,
   GELOSCHT             bit                  null,
   constraint PK_KOMMENTAR primary key (ID)
)
go

/*==============================================================*/
/* Index: REVIEW_COMMENT_FK                                     */
/*==============================================================*/




create nonclustered index REVIEW_COMMENT_FK on KOMMENTAR (REV_ID ASC)
go

/*==============================================================*/
/* Index: COMMENT_COMMENT_FK                                    */
/*==============================================================*/




create nonclustered index COMMENT_COMMENT_FK on KOMMENTAR (KOM_ID ASC)
go

/*==============================================================*/
/* Index: KOMMENTAR_PROFIL_FK                                   */
/*==============================================================*/




create nonclustered index KOMMENTAR_PROFIL_FK on KOMMENTAR (PRO_ID ASC)
go

/*==============================================================*/
/* Table: LISTE                                                 */
/*==============================================================*/
create table LISTE (
   ID                   int                  not null,
   USE_ID               int                  not null,
   OEFFENTLICH          bit                  not null,
   TITEL                varchar(100)         not null,
   ERSTELLUNGSDATUM_B7B39897_7E2D_4EA7_8F52_2A3C5C63A2CC datetime             null default GETDATE(),
   constraint PK_LISTE primary key (ID)
)
go

/*==============================================================*/
/* Index: LIST_USER_FK                                          */
/*==============================================================*/




create nonclustered index LIST_USER_FK on LISTE (USE_ID ASC)
go

/*==============================================================*/
/* Table: NOTIFICATION                                          */
/*==============================================================*/
create table NOTIFICATION (
   ID                   int                  not null,
   PRO_ID               int                  not null,
   TEXT                 varchar(1024)        null,
   GELESEN_AM           datetime             null,
   ERSTELLUNGS_DATUM    datetime             not null default GETDATE(),
   TYP                  NOTIFICATIONTYPE     not null,
   constraint PK_NOTIFICATION primary key (ID)
)
go

/*==============================================================*/
/* Index: PROFIL_NOTIFICATION_FK                                */
/*==============================================================*/




create nonclustered index PROFIL_NOTIFICATION_FK on NOTIFICATION (PRO_ID ASC)
go

/*==============================================================*/
/* Table: PROFIL                                                */
/*==============================================================*/
create table PROFIL (
   NAME                 varchar(1024)        not null,
   "ALTER"              int                  null,
   LAND                 varchar(100)         null,
   BIO                  varchar(1024)        null,
   LOGIN_STATUS         bit                  null,
   ID                   int                  not null,
   USE_ID               int                  not null,
   constraint PK_PROFIL primary key (ID)
)
go

/*==============================================================*/
/* Index: GEHORT_FK                                             */
/*==============================================================*/




create nonclustered index GEHORT_FK on PROFIL (USE_ID ASC)
go

/*==============================================================*/
/* Table: PUBLISHER                                             */
/*==============================================================*/
create table PUBLISHER (
   ID                   int                  not null,
   NAME                 varchar(1024)        not null,
   BESCHREIBUNG         varchar(1024)        null,
   WEBSITE              varchar(1024)        null,
   ERSTELLUNGSDATUM_31C38E9B_D4BC_4B07_A4EB_A48A38517BBC datetime             null default GETDATE(),
   constraint PK_PUBLISHER primary key (ID)
)
go

/*==============================================================*/
/* Table: REVIEW                                                */
/*==============================================================*/
create table REVIEW (
   ID                   int                  not null,
   ZEI_ID               int                  not null,
   GAM_ID               int                  not null,
   PRO_ID               int                  not null,
   FREITEXT             varchar(1024)        null,
   RATING               decimal              not null,
   ERSTELLUNGS_DATUM    datetime             null default GETDATE(),
   AENDERUNGSDATUM      datetime             null,
   GELOSCHT             bit                  null,
   constraint PK_REVIEW primary key (ID)
)
go

/*==============================================================*/
/* Index: REVIEW_GAME_FK                                        */
/*==============================================================*/




create nonclustered index REVIEW_GAME_FK on REVIEW (GAM_ID ASC)
go

/*==============================================================*/
/* Index: REVIEW_TIMESCALE_FK                                   */
/*==============================================================*/




create nonclustered index REVIEW_TIMESCALE_FK on REVIEW (ZEI_ID ASC)
go

/*==============================================================*/
/* Index: REVIEW_PROFIL_FK                                      */
/*==============================================================*/




create nonclustered index REVIEW_PROFIL_FK on REVIEW (PRO_ID ASC)
go

/*==============================================================*/
/* Table: SPIELEACCOUNT                                         */
/*==============================================================*/
create table SPIELEACCOUNT (
   ID                   int                  not null,
   PRO_ID               int                  not null,
   TYP                  ACCOUNTTYP           not null,
   AENDERDATUM          datetime             not null default GETDATE(),
   constraint PK_SPIELEACCOUNT primary key (ID)
)
go

/*==============================================================*/
/* Index: PROFIL_ACCOUNT_FK                                     */
/*==============================================================*/




create nonclustered index PROFIL_ACCOUNT_FK on SPIELEACCOUNT (PRO_ID ASC)
go

/*==============================================================*/
/* Table: SPIELE_RATING                                         */
/*==============================================================*/
create table SPIELE_RATING (
   ID                   int                  not null,
   NAME                 varchar(100)         not null,
   MIN                  decimal              null,
   MAX                  decimal              null,
   SCHRITT              decimal              null,
   ERSTELLUNGS_DATUM    datetime             null default GETDATE(),
   AENDERUNGSDATUM      datetime             null,
   constraint PK_SPIELE_RATING primary key (ID)
)
go

/*==============================================================*/
/* Table: "USER"                                                */
/*==============================================================*/
create table "USER" (
   ID                   int                  not null,
   PRO_ID               int                  null,
   USERNAME             varchar(100)         not null,
   E_MAIL               varchar(1024)        not null,
   PASSWORT             varchar(1024)        not null,
   REGISTRIEUNGSDATUM   datetime             not null default GETDATE(),
   constraint PK_USER primary key (ID)
)
go

/*==============================================================*/
/* Index: GEHORT_FK                                             */
/*==============================================================*/




create nonclustered index GEHORT_FK on "USER" (PRO_ID ASC)
go

/*==============================================================*/
/* Table: USK                                                   */
/*==============================================================*/
create table USK (
   ID                   int                  not null,
   NAME                 varchar(1024)        not null,
   constraint PK_USK primary key (ID)
)
go

/*==============================================================*/
/* Table: ZEITSTAFFEL                                           */
/*==============================================================*/
create table ZEITSTAFFEL (
   ID                   int                  not null,
   EINHEIT              varchar(10)          not null,
   VON                  int                  not null,
   BIS                  int                  not null,
   ERSTELLUNGS_DATUM    datetime             null default GETDATE(),
   AENDERUNGS_DATUM     datetime             null,
   constraint PK_ZEITSTAFFEL primary key (ID)
)
go

alter table BEWERTUNG
   add constraint FK_BEWERTUN_BEWERTUNG_REVIEW foreign key (REV_ID)
      references REVIEW (ID)
go

alter table BEWERTUNG
   add constraint FK_BEWERTUN_BEWERTUNG_PROFIL foreign key (PRO_ID)
      references PROFIL (ID)
go

alter table BILD
   add constraint FK_BILD_GAME_PICT_GAME foreign key (GAM_ID)
      references GAME (ID)
go

alter table BILD
   add constraint FK_BILD_PROFIL_PI_PROFIL foreign key (PRO_ID)
      references PROFIL (ID)
go

alter table BILD
   add constraint FK_BILD_USK_PICTU_USK foreign key (USK_ID)
      references USK (ID)
go

alter table GAME
   add constraint FK_GAME_GAME_GAME_GAME foreign key (GAM_ID)
      references GAME (ID)
go

alter table GAME
   add constraint FK_GAME_GENRE_GAM_GENRE foreign key (GEN_ID)
      references GENRE (ID)
go

alter table GAME
   add constraint FK_GAME_PUBLISHER_PUBLISHE foreign key (PUB_ID)
      references PUBLISHER (ID)
go

alter table GAME
   add constraint FK_GAME_USK_GAME_USK foreign key (USK_ID)
      references USK (ID)
go

alter table GAME_LIST
   add constraint FK_GAME_LIS_GEHÖRT_GAME foreign key (GAM_ID)
      references GAME (ID)
go

alter table GAME_LIST
   add constraint FK_GAME_LIS_GEHÖRT_LISTE foreign key (ID)
      references LISTE (ID)
go

alter table KOMMENTAR
   add constraint FK_KOMMENTA_COMMENT_C_KOMMENTA foreign key (KOM_ID)
      references KOMMENTAR (ID)
go

alter table KOMMENTAR
   add constraint FK_KOMMENTA_KOMMENTAR_PROFIL foreign key (PRO_ID)
      references PROFIL (ID)
go

alter table KOMMENTAR
   add constraint FK_KOMMENTA_REVIEW_CO_REVIEW foreign key (REV_ID)
      references REVIEW (ID)
go

alter table LISTE
   add constraint FK_LISTE_LIST_USER_USER foreign key (USE_ID)
      references "USER" (ID)
go

alter table NOTIFICATION
   add constraint FK_NOTIFICA_PROFIL_NO_PROFIL foreign key (PRO_ID)
      references PROFIL (ID)
go

alter table PROFIL
   add constraint FK_PROFIL_GEHÖRT_USER foreign key (USE_ID)
      references "USER" (ID)
go

alter table REVIEW
   add constraint FK_REVIEW_REVIEW_GA_GAME foreign key (GAM_ID)
      references GAME (ID)
go

alter table REVIEW
   add constraint FK_REVIEW_REVIEW_PR_PROFIL foreign key (PRO_ID)
      references PROFIL (ID)
go

alter table REVIEW
   add constraint FK_REVIEW_REVIEW_TI_ZEITSTAF foreign key (ZEI_ID)
      references ZEITSTAFFEL (ID)
go

alter table SPIELEACCOUNT
   add constraint FK_SPIELEAC_PROFIL_AC_PROFIL foreign key (PRO_ID)
      references PROFIL (ID)
go

alter table "USER"
   add constraint FK_USER_GEHÖRT_PROFIL foreign key (PRO_ID)
      references PROFIL (ID)
go

