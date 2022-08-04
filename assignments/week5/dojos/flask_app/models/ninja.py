from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo
  
class Ninja: 
    DB = 'dojosNinja'
       
    def __init__(self, data):
        self.dojo_id=data['dojo_id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.id = data['id']
    
    @classmethod
    def create_ninja(cls, data):
        query = """
        INSERT INTO ninjas(first_name, last_name,age, dojo_id)
        values (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        ;"""
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def view_all(cls, data):
        query = """
        SELECT * from dojos
        left join ninjas on ninjas.dojo_id = dojos.dojo_id
        where dojo_name=%(dojo_name)s
        ;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        current_dojo = dojo.Dojo(results[0])
        for row in results:
            if row['id'] == None:
                return current_dojo
            ninja_data = {
                'dojo_id': row['ninjas.dojo_id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'age':row['age'],
                'dojo_name':row['dojo_name'],
                'id': row['id']
            }
            current_dojo.ninjas.append(cls(ninja_data))
        return current_dojo
            