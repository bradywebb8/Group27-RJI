#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "", "rjiphotos")

cursor = db.cursor()

# These lines will be used to insert the images data into our database
# sql = """INSERT INTO RJIIMAGES(FILENAME, PHOTOSCORE)
   # VALUES (fileName, photoScore)"""

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)

db.close()