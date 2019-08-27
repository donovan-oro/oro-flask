import sqlite3
from sqlite3 import Error


# first connect to a database, in this case sql lite is already done
# what try does is that it attempts to run a function or process something, if it fails and throws an error, the exepct part will tell you what happened

try:
    # to connect to an db, you need the location, in this case it is a file directly on our systems
    db = sqlite3.connect(r"/Users/novan/Desktop/Oro/pythonsqlite.db")
    # print(sqlite3.version)
except Error as e:
    print(e)


# def create_table():
#     try:
#         cur = db.cursor()
#         cur.execute(
#             '''CREATE TABLE student (StudentID INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT (20) NOT NULL,age INTEGER,marks REAL);''')
#         print('table created successfully')

#     except Error as e:
#         print(e)
#         print('error in operation')
#         db.rollback()
#     # db.close()


# create_table()

# in Databases, a cursor pbject is used to perform create tables and  perform operations on them
cursor = db.cursor()

if __name__ == '__main__':
    print('hi')

    # creates
    # qry = "insert into student (name, age, marks) values('Matt', 27, 90);"

    # try:
    #     cur = db.cursor()
    #     cur.execute(qry)
    #     db.commit()
    #     print("one record added successfully")
    # except:
    #     print("error in operation")
    #     db.rollback()


# READS
    sql = "SELECT name from student;"
    cur = db.cursor()
    cur.execute(sql)
    while True:
        record = cur.fetchone()
        if record == None:
            break
        print(record)
