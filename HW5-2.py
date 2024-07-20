import random

class animals:
    def __init__(self, name, size, name_food, food, habitat, max_age):
        self.name = name
        self.size = size
        self.food = food
        self.name_food = name_food
        self.habitat = habitat
        self.max_age = max_age
        self.kind = []
    
    def new_kind_animal(self, satiety = random.randint(11, 90)):
        self.kind.append([random.choice(['male', 'female']), 0, satiety])

    def status(self):
        print(f'{self.name}, максимальный возраст: {self.max_age}, еда: {self.name_food}, среда обитания: {self.habitat}, вес: {self.size}')
        flag = 0
        for i in self.kind:
            print(f'номер особи: {flag}, пол: {i[0]}, воפраст: {i[1]}, сытость: {i[2]}')
            flag += 1
    
    def reproduce(self, i, j): #размножение
        if i < len(self.kind) and j < len(self.kind) and i != j:
            if self.habitat == 'water' and self.kind[j][2] > 50 and self.kind[i][2] > 50 and self.kind[i][0] != self.kind[j][0]:
                for i in range(12):
                    self.new_kind_animal(23)
            elif self.habitat == 'air' and self.kind[j][2] > 42 and self.kind[i][2] > 42 and self.kind[j][1] > 3 and self.kind[i][1] > 3 and self.kind[i][0] != self.kind[j][0]:
                for i in range(4):
                    self.new_kind_animal(64)
            elif self.habitat == 'earth' and self.kind[j][2] > 20 and self.kind[i][2] > 20 and self.kind[j][1] > 5 and self.kind[i][1] > 5 and self.kind[i][0] != self.kind[j][0]:
                for i in range(2):
                    self.new_kind_animal(73)
            else:
                print("Неудачное размножение")

        else:
            print("Неудачное размножение")

    def delete_kind(self):
        choice = random.choice(self.kind)
        self.kind.remove(choice)
        
    def plus_time(self):
        for animal in self.kind:
            animal[1] += 1


    def is_dead(self):
        plant = 0
        for i in self.kind:
            if i[1] == self.max_age:
                plant += self.size
                self.kind.remove(i)
        return plant
    
    def eat_plant(self, plant):
        if self.food == 'plant' and plant:
            for i in self.kind:
                if plant:
                    plant -= 1
                    i[2] += 26
                else:
                    i[2] -= 9
        return plant
    
    def eat_animal(self):
        for i in self.kind:
            if random.choice([0, 1]):
                eat = random.choice(self.food)
                if eat.kind != []:
                    eat.delete_kind()
                    i[2] += 53
                else:
                    i[2] -= 16
            else:
                i[2] -= 16

    def death_of_hungry(self):
        plant = 0
        for i in self.kind:
            if i[2] < 10:
                plant += self.size
                self.kind.remove(i)
        return plant


    
class Ecosystem:
    def __init__(self):
        self.animals = []
        self.plant = 100

    def status(self):
        print(f"Растительная еда: {self.plant}")
        for i in self.animals:
            i.status()

    def new_kind(self):
        for i in self.animals:
            i.new_kind_animal()
    
    def new_plant(self, amount):
        self.plant += amount
        


    def time(self):
        for animal in self.animals:
            animal.plus_time()
            self.plant += animal.is_dead()
            if animal.food == 'plant':
                self.plant = animal.eat_plant(self.plant)
            else:
                animal.eat_animal()
            self.plant += animal.death_of_hungry()


eco = Ecosystem()

mouse = animals('mouse', 2, 'plant', 'plant', 'earth', 8)
fish = animals('fish', 3, 'plant', 'plant', 'water', 5)
kakadu = animals('parrot', 4, 'plant', 'plant', 'air', 7)
swan = animals('swan', 15, 'plant', 'plant', 'air', 8)
elephant = animals('elephant', 75, 'plant', 'plant', 'earth', 17)
plankton = animals('plankton', 1, 'plant', 'plant', 'water', 2)
bird = animals('bird', 4, ['fish'], [fish], 'air', 6)
tupik = animals('tupik', 3, ['plankton', 'fish'], [plankton, fish], 'air', 6)
whale = animals('whale', 120, ['plankton'], [plankton], 'water', 50)
shark = animals('shark', 20, ['fish', 'plankton'], [fish, plankton], 'water', 6)
hedgehog = animals('hedgehog', 2 , ['mouse'], [mouse], 'earth', 10)
cat = animals('cat', 6, ['mouse', 'fish'], [mouse, fish], 'earth', 15)


eco.animals.append(cat)
eco.animals.append(hedgehog)
eco.animals.append(shark)
eco.animals.append(whale)
eco.animals.append(tupik)
eco.animals.append(bird)
eco.animals.append(plankton)
eco.animals.append(elephant)
eco.animals.append(swan)
eco.animals.append(kakadu)
eco.animals.append(fish)
eco.animals.append(mouse)

eco.new_kind()
eco.new_kind()

while True:
    I = input('Чтобы добавить особь каждого вида нажмите 1,\n Добавить еду 2,\n Просмотреть информацию 3,\n размножить особи 4,\n Моделировать движение времени 5,\n Выйти из программы 6: ')

    if I == '1':
        eco.new_kind()

    elif I == '2':
        amount = int(input("Введите кол-во еды: "))
        eco.new_plant(amount)

    elif I == '3':
        eco.status()

    elif I == '4':
        A = int(input('Чтобы размножить котов введите 0, ежей 1, акул 2, китов 3, тупиков 4, птиц 5, планктонов 6, слонов 7, лебедей 8, какаду 9, рыб 10, мышей 11: '))
        eco.animals[A].status()
        i = int(input('Введите номер особи 1: '))
        j = int(input('Введите номер особи 2: '))
        eco.animals[A].reproduce(i, j)

    elif I == '5':
        eco.time()

    elif I == '6':
        break

    else:
        print("Ошибка")

