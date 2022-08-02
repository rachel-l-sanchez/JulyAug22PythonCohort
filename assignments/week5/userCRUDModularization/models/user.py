from config.mysqlconnection import connectToMySQL

class User:
    
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results_from_db = connectToMySQL('users_schema').query_db(query)
        users = []
        for u in results_from_db:
            users.append(cls(u))
        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(first_name, last_name, email,created_at, updated_at) values(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() + CHAR(10));"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT first_name, last_name, email, created_at, updated_at from users where id=%(id)s;"
        results_from_db = connectToMySQL('users_schema').query_db(query)
        return results_from_db
    
    @classmethod
    def update(cls):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, created_at = NOW(), updated_at=NOW() where id=%(id)s"
        return connectToMySQL('users_schema').query_db(query)
    
    @classmethod
    def delete(cls):
        query = "DELETE from users where id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query)
    