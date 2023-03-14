import mysql.connector

mydb = mysql.connector.connect(user='root', password='azerty', database='laplateforme')
cursor = mydb.cursor()
cursor.execute("SELECT * FROM salles")
salle = []
for i in cursor.fetchall():
    salle.append(i)

print(salle)

# sortie: [(1, 'Lounge', 1, 100), (2, 'Studio son', 1, 5), (3, 'Broadcasting', 2, 50), (4, 'Bocal Peda', 2, 4), (5, 'Coworking', 2, 80), (6, 'Studio Video', 2, 5)]