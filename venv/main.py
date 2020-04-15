import mysql.connector
import sys
import os

db = mysql.connector.connect(
    host="172.104.148.212",
    user="daviid",
    passwd="Ubuntob0I!",
    database="Tfw",
    auth_plugin="mysql_native_password"
)
mycursor = db.cursor()

try:
    mycursor.execute("SELECT password FROM Users")
    result = mycursor.fetchall()

    # connection is not autocommit by default. So you must commit to save
    # your changes.

    newfile = open("Passwordsfromdb.txt","a")
    for row in result:
        newfile.write("\n".join(row))
        newfile.write("\n")

    print(result)
    newfile.close()

finally:
    db.close()