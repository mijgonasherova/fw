class Animal:
    def __init__(self, name, species, birth_date):
        self.name = name
        self.species = species
        self.birth_date = birth_date

    def display_info(self):
        return (
            f"Имя: {self.name}, Вид: {self.species}, Дата рождения: {self.birth_date}"
        )


class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_commands(self, animal):
        return animal.commands


def main_menu():
    registry = AnimalRegistry()
    while True:
        print("1. Завести новое животное")
        print("2. Посмотреть информацию о животном")
        print("3. Выйти")
        choice = input("Выберите опцию: ")
        if choice == "1":
            name = input("Введите имя животного: ")
            species = input("Введите вид животного: ")
            birth_date = input("Введите дату рождения (YYYY-MM-DD): ")
            animal = Animal(name, species, birth_date)
            registry.add_animal(animal)
            print(f"Животное {name} добавлено!")
        elif choice == "2":
            name = input("Введите имя животного: ")
            for animal in registry.animals:
                if animal.name == name:
                    print(animal.display_info())
                    break
            else:
                print("Животное не найдено.")
        elif choice == "3":
            break


if __name__ == "__main__":
    main_menu()
