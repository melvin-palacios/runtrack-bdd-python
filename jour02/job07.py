import mysql.connector

# job07 - Récupérer tous les employés et leur service respectif. Afficher le résultat en console.

"""mydb = mysql.connector.connect(user='root', password='azerty', database='laplateforme')
cursor = mydb.cursor()
query = "SELECT employes.nom, employes.prenom, employes.salaire,\
            services.nom FROM employes INNER JOIN services ON employes.id_service = services.id;"
cursor.execute(query)
print(cursor.fetchall())"""
class EmployeManager:
    def __init__(self, user, password, database, host='localhost'):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (nom, prenom, salaire, id_service)"
        self.cursor.execute(query)
        return self.cursor.lastrowid

    def get_employe(self, id):
        query = "SELECT * FROM employes WHERE id"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            return {
                'id': result[0],
                'nom': result[1],
                'prenom': result[2],
                'salaire': result[3],
                'service_id': result[4]
            }
        else:
            return None

    def update_employe(self, id, nom=None, prenom=None, salaire=None, service_id=None):
        employe = self.get_employe(id)
        if not employe:
            return False
        query = "UPDATE employes SET "
        values = []
        if nom is not None:
            query += "nom = %s, "
            values.append(nom)
        if prenom is not None:
            query += "prenom = %s, "
            values.append(prenom)
        if salaire is not None:
            query += "salaire = %s, "
            values.append(salaire)
        if service_id is not None:
            query += "service_id = %s, "
            values.append(service_id)
        query = query[:-2] + " WHERE id = %s"
        values.append(id)
        self.cursor.execute(query, values)
        self.connection.commit()
        return True

    def delete_employe(self, id):
        query = "DELETE FROM employes WHERE id"
        self.cursor.execute(query)
        self.connection.commit()
        return True

    def get_all_employes(self):
        query = "SELECT employes.*, services.nom AS service FROM employes INNER JOIN services ON employes.id_service = services.id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        employes = []
        for row in result:
            employes.append({
                'id': row[0],
                'nom': row[1],
                'prenom': row[2],
                'salaire': row[3],
                'service_id': row[4],
                'service': row[5]
            })
        return employes


employe_manager = EmployeManager('root', 'azerty', 'laplateforme')
print(employe_manager.get_all_employes())
