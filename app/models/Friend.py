from system.core.model import Model

class Friend(Model):
    def __init__(self):
        super(Friend, self).__init__()

    def get_all_friends(self):
        query = "SELECT * FROM friends"
        all_friends = self.db.query_db(query)
        return all_friends

    def get_friend_by_id(self, f_id):
        query = "SELECT * FROM friends WHERE id=:id"
        in_data = {
            'id': f_id['id'] 
        }
        friend = self.db.query_db(query, in_data)
        return friend

    def update_friend(self, in_data):
        #Input validation
        query = "UPDATE friends SET firstname=:firstname, lastname=:lastname, occupation=:occupation, knownfor=:knownfor, updated_at=NOW()" \
                "WHERE id=:id"
        self.db.query_db(query, in_data)
        return in_data['id']

    def delete_friend(self, f_id):
        in_data = {
            'id': f_id['id']
        }
        query = "DELETE FROM friends WHERE id=:id"
        self.db.query_db(query, in_data)
        return

    def new_friend(self, in_data):
            #Input validation
            query = "INSERT INTO friends (firstname, lastname, occupation, knownfor, created_at, updated_at) " \
                    "VALUES (:firstname, :lastname, :occupation, :knownfor, NOW(), NOW())"
            friend_id = self.db.query_db(query, in_data)
            return friend_id