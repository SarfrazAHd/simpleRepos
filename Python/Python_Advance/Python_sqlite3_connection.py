



import sqlite3

db = sqlite3.connect("C:/Users/Nizam/Database/Student_database.db")
curs = db.cursor()

sql = "SELECT * FROM Student_db WHERE F_name like?"
x = "sarfraz"


res = curs.execute(sql, (x,))

for i in res:
    print(i, end=" ")