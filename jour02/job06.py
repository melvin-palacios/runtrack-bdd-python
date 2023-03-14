import mysql.connector

mydb = mysql.connector.connect(user='root', password='azerty', database='laplateforme')
cursor = mydb.cursor()
cursor.execute("SELECT SUM(capacite) FROM salles;")
superficie = cursor.fetchall()[0][0]
print('La capacite totale de toute les salles est de', superficie)

