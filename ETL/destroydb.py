import sqlite3

connection=sqlite3.connect('covid.db')

c=connection.cursor()

c.execute("""DROP TABLE REGION""")
c.execute("""DROP TABLE TESTS""")
c.execute("""DROP TABLE HOSPITALS""")
c.execute("""DROP TABLE HOSPITAL_STAFF""")

connection.commit()

connection.close()