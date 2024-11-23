class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        if args:
            cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.number_of_floors_list = []

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __del__(self):
        print(f'{self.name} снесен,но он останется в истории')

    def __len__(self):
        '''Количество этажей'''
        return self.number_of_floors

    def __str__(self):
        '''Полная информация'''
        return f'Название {self.name}\nКоличество этажей {self.number_of_floors}'

    def __eq__(self, other):
        '''Сравнение ='''
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        '''сравнение (<)'''
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        '''Сравнение (<=)'''
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        '''Сравнение (>)'''
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        '''Сравнение (>=)'''
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other):
        '''Сравнение (!=)'''
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return NotImplemented

    def __add__(self, value):
        '''Увеличиваем количество этажей'''
        if isinstance(value, (int, float)):
            self.number_of_floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        '''Добавоем количестов этажей через метод __ad__'''
        return self.__add__(value)

    def __iadd__(self, value):
        '''Добавляем количество этажей в список '''
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

