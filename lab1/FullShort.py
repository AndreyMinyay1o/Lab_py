# Пункт 7: Методы для вывода и сравнения объектов
class Reader:
    # (Прочие методы остаются как в предыдущих пунктах)

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
