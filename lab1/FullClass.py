import re
import json


# Пункт 3: Класс Reader (с инкапсуляцией и валидацией)
class Reader:
    def __init__(self, surname, name, patronymic, address, phone):
        self.surname = surname  # Вставим значения через свойство
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.phone = phone

    # Инкапсуляция полей
    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if not value.isalpha():
            raise ValueError("Фамилия должна содержать только буквы.")
        self._surname = value.capitalize()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("Имя должно содержать только буквы.")
        self._name = value.capitalize()

    @property
    def patronymic(self):
        return self._patronymic

    @patronymic.setter
    def patronymic(self, value):
        if not value.isalpha():
            raise ValueError("Отчество должно содержать только буквы.")
        self._patronymic = value.capitalize()

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if len(value) < 5:
            raise ValueError("Адрес должен быть не менее 5 символов.")
        self._address = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not re.match(r'^\+?\d{10,15}$', value):
            raise ValueError("Телефон должен быть в формате +XXXXXXXXXXX.")
        self._phone = value

    # Статические методы для валидации
    @staticmethod
    def validate_surname(surname):
        if not surname.isalpha():
            raise ValueError("Фамилия должна содержать только буквы.")
        return surname.capitalize()

    @staticmethod
    def validate_name(name):
        if not name.isalpha():
            raise ValueError("Имя должно содержать только буквы.")
        return name.capitalize()

    @staticmethod
    def validate_patronymic(patronymic):
        if not patronymic.isalpha():
            raise ValueError("Отчество должно содержать только буквы.")
        return patronymic.capitalize()

    @staticmethod
    def validate_address(address):
        if len(address) < 5:
            raise ValueError("Адрес должен быть не менее 5 символов.")
        return address

    @staticmethod
    def validate_phone(phone):
        if not re.match(r'^\+?\d{10,15}$', phone):
            raise ValueError("Телефон должен быть в формате +XXXXXXXXXXX.")
        return phone

    # Методы для вывода и сравнения объектов
    def full_version(self):
        return f"Читатель: {self.surname} {self.name} {self.patronymic}, Адрес: {self.address}, Телефон: {self.phone}"

    def short_version(self):
        return f"{self.surname} {self.name[0]}. {self.patronymic[0]}."

    def __eq__(self, other):
        return (self.surname == other.surname and
                self.name == other.name and
                self.patronymic == other.patronymic and
                self.address == other.address and
                self.phone == other.phone)

    # Метод для вывода объекта в формате JSON
    def to_json(self):
        return json.dumps({
            "surname": self.surname,
            "name": self.name,
            "patronymic": self.patronymic,
            "address": self.address,
            "phone": self.phone
        }, ensure_ascii=False)


# Пункт 8: Класс для краткой версии данных
class ShortReader:
    def __init__(self, reader):
        self.surname = reader.surname
        self.initials = f"{reader.name[0]}. {reader.patronymic[0]}."

    def __str__(self):
        return f"{self.surname} {self.initials}"


# Пункт 9: Иерархия классов
class ExtendedReader(Reader, ShortReader):
    def __init__(self, surname, name, patronymic, address, phone):
        # Инициализация из Reader
        Reader.__init__(self, surname, name, patronymic, address, phone)
        # Инициализация из ShortReader
        ShortReader.__init__(self, self)


# Пример использования
if __name__ == "__main__":
    try:
        # Создаем объект читателя
        reader = Reader("Иванов", "Иван", "Иванович", "ул. Ленина, д. 1", "+79991234567")

        # Выводим полную и краткую версию
        print(reader.full_version())  # Полная версия
        print(reader.short_version())  # Краткая версия

        # Выводим JSON-версию
        print(reader.to_json())  # Вывод в формате JSON

        # Создаем объект краткой версии
        short_reader = ShortReader(reader)
        print(short_reader)  # Вывод краткой версии через ShortReader

        # Создаем объект расширенной версии
        extended_reader = ExtendedReader("Петров", "Петр", "Петрович", "ул. Октябрьская, д. 2", "+79998765432")
        print(extended_reader.full_version())  # Полная версия расширенного читателя
        print(extended_reader.short_version())  # Краткая версия расширенного читателя

    except ValueError as e:
        print(f"Ошибка: {e}")
