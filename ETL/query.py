import sqlite3
"""WE can use this python file to query our database to make visuals/analytics"""
connection=sqlite3.connect('backend/covid.db')

c=connection.cursor()

#c.execute("""SELECT * FROM HOSPITALS h inner join REGION r on r.id=h.region_id WHERE r.code='SK022' """)
c.execute("""SELECT * FROM HOSPITAL_STAFF""")

print(c.fetchall())

connection.commit()

connection.close()