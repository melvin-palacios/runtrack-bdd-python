import mysql.connector

mydb = mysql.connector.connect(user='root', password='azerty', database='laplateforme')
cursor = mydb.cursor()
cursor.execute("SELECT SUM(superficie) FROM etage;")
superficie = cursor.fetchall()[0][0]
print('La superficie totale est de', superficie, 'm²')

