
import time
current_time = time.strftime("%H")
current_month = time.strftime("%B")
print('Сейчас {}, время {} час(ов)'.format(current_month, current_time))

class animals:
    feeding_status = 'hungry'
    name = 'Имя'
    weight = 0 
    def feed(self): 
        self.feeding_status = 'fed'
    if current_time == '07' or current_time == '17':
        print('Время покормить животных!')
        feed = input('Покормить? Введите "да" ')
        if feed == "да":
            feed(self)
            print('Животные накормлены')
    def count_weight(*args):
        weights = [self.weight]
        print(sum(weights)) 

class birds(animals):
    egg_status = 'in process'
    def take_eggs(self):
        self.egg_status = 'taken'
    if current_time == '12':
        print('Время собрать яйца!')
        take = input('Собрать? Введите "да" ')
        if take == "да":
            take_eggs(self)
            print('Яйца собраны')

class geese(birds):
    sound = 'Гаа'
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class chics(birds):
    sound = 'Кококо'
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class ducks(birds):
    sound = 'Кря'
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
class mammals(animals):
    milk_status = 'in process'
    def take_milk(self):
        self.milk_status = 'milk taken'
    if current_time == '08':    
        print('Время собрать молоко!')
        milk = input('Подоить? Введите "да" ')
        if milk == "да":
            take_milk(self)
            print('Молоко собрано')

class cows(mammals):
    sound = 'Myyy'
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class goats(mammals):
    sound = 'Mee'
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class woolen(animals):
    wool_status = 'in process'  
    def cut_wool(self):
        self.wool_status = 'wool taken'
    if current_month == 'November' or current_month == 'May':        
        print('Время стричь шерсть!')
        cut = input('Стричь? Введите "да" ')
        if cut == 'да':
            cut_wool(self)
            print('Шерсть сострижена')

class sheep(woolen):
    sound = 'Беее'
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


goose0 = geese('Серый', 6.5)
goose1 = geese('Белый', 7.0)

cow0 = cows('Манька', 550.0)

sheep0 = sheep('Барашек', 80.6)
sheep1 = sheep('Кудрявый', 94.0)

chic0 = chics('Ко-ко', 1.2)
chic1 = chics('Кукареку', 1.1)

goat0 = goats('Рога', 52.7)
goat1 = goats('Копыта', 56.3)

duck0 = ducks('Кряква', 3.4)

count_weight(goose0, goose1, cow0, sheep0, sheep1, chic0, chic1, goat0, goat1, duck0)

