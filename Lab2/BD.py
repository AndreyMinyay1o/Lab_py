import mysql.connector

class MyEntity_rep_DB:
    def init(self, db_config):
        self.db_config = db_config
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor(dictionary=True)

    def get_by_id(self, entity_id):
        query = "SELECT * FROM my_entities WHERE ID = %s"
        self.cursor.execute(query, (entity_id,))
        return self.cursor.fetchone()

    def get_k_n_short_list(self, k, n):
        query = f"SELECT * FROM my_entities LIMIT {k * (n - 1)}, {k}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add(self, new_object):
        new_object["ID"] = str(uuid.uuid4())
        query = "INSERT INTO my_entities (ID, Field1, Field2) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (new_object["ID"], new_object["Field1"], new_object["Field2"]))
        self.conn.commit()

    def replace_by_id(self, entity_id, new_object):
        query = "UPDATE my_entities SET Field1 = %s, Field2 = %s WHERE ID = %s"
        self.cursor.execute(query, (new_object["Field1"], new_object["Field2"], entity_id))
        self.conn.commit()

    def remove_by_id(self, entity_id):
        query = "DELETE FROM my_entities WHERE ID = %s"
        self.cursor.execute(query, (entity_id,))
        self.conn.commit()

    def get_count(self):
        query = "SELECT COUNT(*) FROM my_entities"
        self.cursor.execute(query)
        return self.cursor.fetchone()["COUNT(*)"]