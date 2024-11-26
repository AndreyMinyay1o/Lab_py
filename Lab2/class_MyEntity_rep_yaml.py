def init(self, filename):
    self.filename = filename
    self.load_data()


def load_data(self):
    try:
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.data = yaml.safe_load(file) or []
    except FileNotFoundError:
        self.data = []


def save_data(self):
    with open(self.filename, 'w', encoding='utf-8') as file:
        yaml.dump(self.data, file, allow_unicode=True)

    # Чтение всех значений из файла


def get_all(self):
    return self.data
# Запись всех значений в файл
    def write_all(self, new_data):
        self.data = new_data
        self.save_data()

    # Получить объект по ID
    def get_by_id(self, entity_id):
        for item in self.data:
            if item["ID"] == entity_id:
                return item
        return None

    # Получить список k по счету n объектов класса short
    def get_k_n_short_list(self, k, n):
        return self.data[(n - 1) * k:n * k]

    # Сортировка элементов по выбранному полю
    def sort_by_field(self, field):
        self.data.sort(key=lambda x: x.get(field))

    # Добавить объект в список (при добавлении формируем новый ID)
    def add(self, new_object):
        new_object["ID"] = str(uuid.uuid4())
        self.data.append(new_object)
        self.save_data()

    # Заменить элемент списка по ID
    def replace_by_id(self, entity_id, new_object):
        for i, item in enumerate(self.data):
            if item["ID"] == entity_id:
                self.data[i] = new_object
                self.save_data()
                return True
        return False

    # Удалить элемент списка по ID
    def remove_by_id(self, entity_id):
        for i, item in enumerate(self.data):
            if item["ID"] == entity_id:
                del self.data[i]
                self.save_data()
                return True
        return False

    # Получить количество элементов
    def get_count(self):
        return len(self.data)