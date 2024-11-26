class DBAdapter:
    def init(self, db_rep):
        self.db_rep = db_rep

    # Адаптация метода get_all
    def get_all(self):
        query = "SELECT * FROM my_entities"
        self.db_rep.cursor.execute(query)
        return self.db_rep.cursor.fetchall()

    # Адаптация метода write_all
    def write_all(self, new_data):
        for item in new_data:
            if not item["ID"]:
                item["ID"] = str(uuid.uuid4())  # Генерация нового ID, если он отсутствует
            query = "INSERT INTO my_entities (ID, Field1, Field2) VALUES (%s, %s, %s)"
            self.db_rep.cursor.execute(query, (item["ID"], item["Field1"], item["Field2"]))
        self.db_rep.conn.commit()

    # Адаптация метода get_by_id
    def get_by_id(self, entity_id):
        return self.db_rep.get_by_id(entity_id)

    # Адаптация метода get_k_n_short_list
    def get_k_n_short_list(self, k, n):
        return self.db_rep.get_k_n_short_list(k, n)

    # Адаптация метода add
    def add(self, new_object):
        self.db_rep.add(new_object)

    # Адаптация метода replace_by_id
    def replace_by_id(self, entity_id, new_object):
        self.db_rep.replace_by_id(entity_id, new_object)

    # Адаптация метода remove_by_id
    def remove_by_id(self, entity_id):
        self.db_rep.remove_by_id(entity_id)

    # Адаптация метода get_count
    def get_count(self):
        return self.db_rep.get_count()