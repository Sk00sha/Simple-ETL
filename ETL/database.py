import sqlite3


connection=sqlite3.connect('covid.db')

c=connection.cursor()

c.execute("""CREATE TABLE REGION(
        id INTEGER PRIMARY KEY,
        title   text,
        code text,
        abbreviation text
)""")

c.execute("""CREATE TABLE TESTS(
        id INTEGER PRIMARY KEY,
        positivity_rate   REAL,
        date_updated text,
        positive INTEGER,
        negative INTEGER
)""")
c.execute("""CREATE TABLE HOSPITALS(
        id INTEGER PRIMARY KEY,
        region_id INTEGER,
        free_all INTEGER,
        occupied_jis_covid INTEGER,
        occupied_oaim_covid INTEGER,
        occupied_o2_covid INTEGER,
        occupied_other_covid INTEGER,
        updated_at text,
        FOREIGN KEY (region_id)
        REFERENCES REGION (id)
)""")
c.execute("""CREATE TABLE HOSPITAL_STAFF(
        id INTEGER PRIMARY KEY,
        hospital_id INTEGER,
        oow_doctors INTEGER,
        oow_nurses INTEGER,
        oow_other INTEGER,
        FOREIGN KEY (hospital_id)
        REFERENCES HOSPITALS (id)
)""")


connection.commit()

connection.close()

