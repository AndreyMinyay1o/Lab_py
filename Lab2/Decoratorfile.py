class FileFilterSortDecorator:
    def init(self, file_rep, filter_func=None, sort_func=None):
        self.file_rep = file_rep
        self.filter_func = filter_func
        self.sort_func = sort_func

    def get_k_n_short_list(self, k, n):
        result = self.file_rep.get_k_n_short_list(k, n)

        # Применяем фильтрацию, если она передана
        if self.filter_func:
            result = filter(self.filter_func, result)

        # Применяем сортировку, если она передана
        if self.sort_func:
            result = sorted(result, key=self.sort_func)

        return list(result)

    def get_count(self):
        result = self.file_rep.get_count()

        # Применяем фильтрацию, если она передана
        if self.filter_func:
            result = filter(self.filter_func, result)

        return len(list(result))

        def write_all(self, new_data):
            for item in new_data:
                if not item["ID"]:
                    item["ID"] = str(uuid.uuid4())  # Генерация нового ID
                self.data.append(item)
            self.save_data()

        def get_by_id(self, entity_id):
            return next((item for item in self.data if item["ID"] == entity_id), None)

        def get_k_n_short_list(self, k, n):
            return self.data[k * n: (k + 1) * n]

        def sort_by_field(self, field):
            return sorted(self.data, key=lambda x: x.get(field, ''))

        def add(self, new_object):
            if not new_object["ID"]:
                new_object["ID"] = str(uuid.uuid4())
            self.data.append(new_object)
            self.save_data()

        def replace_by_id(self, entity_id, new_object):
            for idx, item in enumerate(self.data):
                if item["ID"] == entity_id:
                    self.data[idx] = new_object
                    self.save_data()
                    break

        def remove_by_id(self, entity_id):
            self.data = [item for item in self.data if item["ID"] != entity_id]
            self.save_data()

        def get_count(self):
            return len(self.data)

    class MyEntity_rep_DB:
        def init(self, db_name="my_database.db"):
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_table()

        def create_table(self):
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS my_entities (
                ID TEXT PRIMARY KEY,
                Field1 TEXT,
                Field2 TEXT
            )''')
            self.conn.commit()

        def get_all(self):
            self.cursor.execute("SELECT * FROM my_entities")
            return self.cursor.fetchall()

        def write_all(self, new_data):
            for item in new_data:
                if not item["ID"]:
                    item["ID"] = str(uuid.uuid4())  # Генерация нового ID
                self.cursor.execute("INSERT INTO my_entities (ID, Field1, Field2) VALUES (?, ?, ?)",
                                    (item["ID"], item["Field1"], item["Field2"]))
            self.conn.commit()

        def get_by_id(self, entity_id):
            self.cursor.execute("SELECT * FROM my_entities WHERE ID=?", (entity_id,))
            return self.cursor.fetchone()

        def get_k_n_short_list(self, k, n):
            self.cursor.execute(f"SELECT * FROM my_entities LIMIT {n} OFFSET {k * n}")
            return self.cursor.fetchall()

        def add(self, new_object):
            if not new_object["ID"]:
                new_object["ID"] = str(uuid.uuid4())
            self.cursor.execute("INSERT INTO my_entities (ID, Field1, Field2) VALUES (?, ?, ?)",
                                (new_object["ID"], new_object["Field1"], new_object["Field2"]))
            self.conn.commit()

        def replace_by_id(self, entity_id, new_object):
            self.cursor.execute("UPDATE my_entities SET Field1=?, Field2=? WHERE ID=?",
                                (new_object["Field1"], new_object["Field2"], entity_id))
            self.conn.commit()

        def remove_by_id(self, entity_id):
            self.cursor.execute("DELETE FROM my_entities WHERE ID=?", (entity_id,))
            self.conn.commit()

        def get_count(self):
            self.cursor.execute("SELECT COUNT(*) FROM my_entities")
            return self.cursor.fetchone()[0]D