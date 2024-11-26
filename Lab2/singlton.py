class DBConnection:
    _instance = None

    def new(cls, db_config):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).new(cls)
            cls._instance.conn = mysql.connector.connect(**db_config)
            cls._instance.cursor = cls._instance.conn.cursor(dictionary=True)
        return cls._instance