class DBAdapter:
    def init(self, db_rep):
        self.db_rep = db_rep

    def get_all(self):
        return self.db_rep.get_all()

    def write_all(self, new_data):
        self.db_rep.write_all(new_data)

    def get_by_id(self, entity_id):
        return self.db_rep.get_by_id(entity_id)

    def get_k_n_short_list(self, k, n):
        return self.db_rep.get_k_n_short_list(k, n)

    def add(self, new_object):
        self.db_rep.add(new_object)

    def replace_by_id(self, entity_id, new_object):
        self.db_rep.replace_by_id(entity_id, new_object)

    def remove_by_id(self, entity_id):
        self.db_rep.remove_by_id(entity_id)

        def get_count(self):
            return self.db_rep.get_count()