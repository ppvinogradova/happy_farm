import time 

current_time = time.strftime("%H")
current_month = time.strftime("%B")
print('Сейчас {}, время {} час(ов)'.format(current_month, current_time))

class animals:
    feeding_status = 'hungry'
    name = 'Имя'
    weight = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self): 
        if current_time == '07' or current_time == '17':
            print(f'{self.name} хочет кушать!')
            feed = input('Покормить? Введите "да" ')
            if feed == "да":
                self.feeding_status = 'fed'
                print('Животное накормлено')

class birds(animals):
    egg_status = 'in process'
    def take_eggs(self):
        if current_time == '12':
            print(f'Время собрать яйца у {self.name}!')
            take = input('Собрать? Введите "да" ')
            if take == "да":
                self.egg_status = 'taken'
                print('Яйца собраны')

class geese(birds):
    sound = 'Гаа'
    ind = 'гусь'
    
class chics(birds):
    sound = 'Кококо'
    ind = 'курица'

class ducks(birds):
    sound = 'Кря'
    ind = 'утка'
    
class mammals(animals):
    milk_status = 'in process'
    def take_milk(self):
        if current_time == '08':    
            print(f'Время подоить {self.name}!')
            milk = input('Подоить? Введите "да" ')
            if milk == "да":
                self.milk_status = 'milk taken'
                print('Молоко собрано')

class cows(mammals):
    sound = 'Мууу'
    ind = 'корова'

class goats(mammals):
    sound = 'Mee'
    ind = 'коза'

class woolen(animals):
    wool_status = 'in process'  
    def cut_wool(self):  
        if current_month == 'November' or current_month == 'May':        
            print(f'Время стричь {self.name}!')
            cut = input('Стричь? Введите "да" ')
            if cut == 'да':
                self.wool_status = 'wool taken'
                print('Шерсть сострижена')

class sheep(woolen):
    sound = 'Беее'
    ind = 'баран'

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

animal_list = [goose0, goose1, cow0, sheep0, sheep1, chic0, chic1, goat0, goat1, duck0]
sum_weight = 0
weights_list = []
sound_list = []
for a in animal_list:
    sum_weight += a.weight
    weights_list.append(a.weight)
    sound_list.append(a.sound)
    a.feed()
    if isinstance(a,cows) == True or isinstance(a,goats) == True:
        a.take_milk()
    elif isinstance(a,sheep) == True:
        a.cut_wool()
    elif isinstance(a,chics) == True or isinstance(a,ducks) == True or isinstance(a,geese) == True:
        a.take_eggs()   
print(f'Общий вес животных равен {round(sum_weight, 2)}')
d = dict(zip(animal_list, weights_list))
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
big = get_key(d, max(weights_list))
print(f'Самое тяжелое живтоное - {big.name}')
sounds = dict(zip(animal_list, sound_list))
hear = input('Что вы слышите? ')
for s in sounds.values():
    if s == hear:
        print(f'Должно быть, это {get_key(sounds, s).ind}')
        break




    