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
            print('Время покормить животных!')
            feed = input('Покормить? Введите "да" ')
            if feed == "да":
                self.feeding_status = 'fed'
                print('Животные накормлены')

class birds(animals):
    egg_status = 'in process'
    def take_eggs(self):
        if current_time == '12':
            print('Время собрать яйца!')
            take = input('Собрать? Введите "да" ')
            if take == "да":
                self.egg_status = 'taken'
                print('Яйца собраны')

class geese(birds):
    sound = 'Гаа'
    
class chics(birds):
    sound = 'Кококо'

class ducks(birds):
    sound = 'Кря'
    
class mammals(animals):
    milk_status = 'in process'
    def take_milk(self):
        if current_time == '08':    
            print('Время собрать молоко!')
            milk = input('Подоить? Введите "да" ')
            if milk == "да":
                self.milk_status = 'milk taken'
                print('Молоко собрано')

class cows(mammals):
    sound = 'Myyy'

class goats(mammals):
    sound = 'Mee'

class woolen(animals):
    wool_status = 'in process'  
    def cut_wool(self):  
        if current_month == 'November' or current_month == 'May':        
            print('Время стричь шерсть!')
            cut = input('Стричь? Введите "да" ')
            if cut == 'да':
                self.wool_status = 'wool taken'
                print('Шерсть сострижена')

class sheep(woolen):
    sound = 'Беее'

goose0 = geese('Серый', 6.5)
goose1 = geese('Белый', 7.0)

cow0 = cows('Манька', 550.0)

sheep0 = sheep('Барашек', 80.6)
sheep1 = sheep('Кудрявый', 94.0)
feed(cow0)
chic0 = chics('Ко-ко', 1.2)
chic1 = chics('Кукареку', 1.1)

goat0 = goats('Рога', 52.7)
goat1 = goats('Копыта', 56.3)

duck0 = ducks('Кряква', 3.4)

animal_list = [goose0, goose1, cow0, sheep0, sheep1, chic0, chic1, goat0, goat1, duck0]
sum_weight = 0
weights_list = []
for a in animal_list:
    sum_weight += a.weight
    weights_list.append(a.weight)
print(f'Общий вес животных равен {round(sum_weight, 2)}')
d = dict(zip(animal_list, weights_list))
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
big = get_key(d, max(weights_list))
print(big.name)





    