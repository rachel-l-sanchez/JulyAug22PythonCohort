from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = 'dojosNinja'
    
    def __init__(self, data):
        self.dojo_id=data['dojo_id']
        self.dojo_name=data['dojo_name']
        
        self.ninjas=[]
        
    @classmethod
    def create_dojo(cls, data):
        query = """
        INSERT INTO dojos(dojo_name)
        values(%(dojo_name)s)
        ;"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * from dojos;"
        results_from_db = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for d in results_from_db:
            dojos.append(cls(d))
        return dojos