from config.mysqlconnection import connectToMySQL
from models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    @classmethod
    def guardar(cls,data):
        query = "INSERT INTO dojos (name,created_at,updated_at) VALUES (%(nombre)s,NOW(),NOW());"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db =  connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        dojos=[]
        for d in dojos_from_db:
            dojos.append(cls(d))
        return dojos
    
    @classmethod
    def get_dojo_by_id(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id=%(id)s;"
        dojo_from_db = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
        print (dojo_from_db)
        return cls(dojo_from_db[0])
    
    @classmethod
    def get_ninjas_from_dojo(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
        dojo = cls(results[0])
        for datos in results:
            ninja_data = {
                "id": datos['id'],
                "dojo_id": datos['dojo_id'],
                "first_name": datos['first_name'],
                "last_name": datos['last_name'],
                "age": datos['age'],
                "created_at": datos['created_at'],
                "updated_at": datos['updated_at']
            }
            dojo.ninjas.append( Ninja( ninja_data ) )
        return dojo.ninjas
    
    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(nombre)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)