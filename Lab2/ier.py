class MyEntity_rep(MyEntity_rep_json, MyEntity_rep_yaml):
    def init(self, filename, file_format='json'):
        if file_format == 'json':
            MyEntity_rep_json.init(self, filename)
        elif file_format == 'yaml':
            MyEntity_rep_yaml.init(self, filename)
        else:
            raise ValueError("Unsupported file format. Use 'json' or 'yaml'.")