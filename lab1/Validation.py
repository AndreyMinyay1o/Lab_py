# Пункт 4: Методы валидации
class Reader:
    # (Прочие методы остаются как в пункте 3)

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
