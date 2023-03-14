import mysql.connector

mydb = mysql.connector.connect(user='root', password='azerty', database='laplateforme')
cursor = mydb.cursor()
cursor.execute("SELECT * FROM `laplateforme`.`etudiants`")

for i in cursor.fetchall():
    print(i)

