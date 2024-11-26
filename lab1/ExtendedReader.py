
# Пункт 9: Иерархия классов
class ExtendedReader(Reader, ShortReader):
    def __init__(self, surname, name, patronymic, address, phone):
        # Инициализация из Reader
        Reader.__init__(self, surname, name, patronymic, address, phone)
        # Инициализация из ShortReader
        ShortReader.__init__(self, self)
