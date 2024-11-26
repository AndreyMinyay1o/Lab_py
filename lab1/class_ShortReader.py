# Пункт 8: Класс для краткой версии данных
class ShortReader:
    def __init__(self, reader):
        self.surname = reader.surname
        self.initials = f"{reader.name[0]}. {reader.patronymic[0]}."

    def __str__(self):
        return f"{self.surname} {self.initials}"
