



import sqlite3

db = sqlite3.connect("C:/Users/Nizam/Database/Student_database.db")
curs = db.cursor()

sql = " SELECT * FROM Student_db "
res = curs.execute(sql)

for i in res:
    print(i, end=" ")