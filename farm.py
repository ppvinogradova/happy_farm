
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

class chics(birds):
    sound = 'Кококо'

class ducks(birds):
    sound = 'Кря'
    
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

class goats(mammals):
    sound = 'Mee'

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


goose0 = geese()
goose0.name = 'Серый'
goose0.weight = 6.5 #kg
goose1 = geese()
goose1.name = 'Белый'
goose1.weight = 7.0 #kg

cow0 = cows()
cow0.name = 'Манька'
cow0.weight = 550.0 #kg

sheep0 = sheep()
sheep0.name = 'Барашек'
sheep0.weight = 80.6 #kg
sheep1 = sheep()
sheep1.name = 'Кудрявый'
sheep1.weight = 94.0 #kg

chic0 = chics()
chic0.name = 'Ко-ко'
chic0.weight = 1.2 #kg
chic1 = chics()
chic1.name = 'Кукареку'
chic1.weight = 1.1 #kg

goat0 = goats()
goat0.name = 'Рога'
goat0.weight = 52.7 #kg
goat1 = goats()
goat1.name = 'Копыта'
goat1.weight = 56.3 #kg

duck0 = ducks()
duck0.name = 'Кряква'
duck0.weight = 3.4 #kg
count_weight(goose0, goose1, cow0, sheep0, sheep1, chic0, chic1, goat0, goat1, duck0)

