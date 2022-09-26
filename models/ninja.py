from config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def guardar(cls,data):
        query = "INSERT INTO ninjas (dojo_id,first_name,last_name,age,created_at,updated_at) VALUES (%(dojo_id)s,%(nombre)s,%(apellido)s,%(edad)s,NOW(),NOW());"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_from_db =  connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        ninjas =[]
        for n in ninjas_from_db:
            ninjas.append(cls(n))
        return ninjas
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        ninja_from_db = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
        return cls(ninja_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(nombre)s, last_name=%(apellido)s, age=%(edad)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)