class Animal:
    def __init__(self, name, birth_date):
        self._name = name
        self._birth_date = birth_date

    def display_info(self):
        return f"Имя: {self._name}, Дата рождения: {self._birth_date}"


class DomesticAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)


class PackAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
