class Tree:
    def __init__(self, height, trunk_diameter_cm):
        self.height = height
        self.trunk_diameter_cm = trunk_diameter_cm
        self.number_of_leaves = height * trunk_diameter_cm * 100
        if height <= 0 or height > 150:
            raise ValueError("Неправильне значення. Вкажіть висоту від 0 до 150")
        if trunk_diameter_cm <= 0 or trunk_diameter_cm > 1000:
            raise ValueError("Неправильне значення. Вкажіть діаметр від 0 до 1000")

    def grow(self):
        self.height = self.height + 0.5
        self.trunk_diameter_cm = self.trunk_diameter_cm + 2

    def leaf_fall(self):
        self.number_of_leaves = self.number_of_leaves * 0.7

    def info(self):
        print(self.height, self.trunk_diameter_cm, self.number_of_leaves)


try:
    apple = Tree(4, 2)
    apple.grow()
    apple.leaf_fall()
    apple.info()

except ValueError as e:
    print(f"Помилка: {e}")


class Kettle:
    def __init__(self, volume, current_volume, water_temperature=20, on=False):
        self.volume = volume
        self.current_volume = current_volume
        self.water_temperature = water_temperature
        self.on = on
        if volume < 0.5 or volume > 5:
            raise ValueError("Неправильне значення. Вкажіть об'єм від 0,5 до 5")
        if current_volume > volume or current_volume < 0:
            raise ValueError("Поточний об'єм не може перевищувати об'єм і не може бути меншим за 0")

    def pour_water(self, amount):
        available_volume = self.volume - self.current_volume
        if amount > available_volume:
            raise ValueError("Неможливо додати кількість води, що перевищує доступний об'єм. Вода з чайника переллється"
                             ".")
        if amount == 0:
            raise ValueError("Неможливо налити води в чайник з порожнього стакану")
        self.current_volume = self.current_volume + amount

    def drain_water(self, amount):
        if amount > self.current_volume:
            raise ValueError("Неможливо злити більшу кількість води, ніж є у чайнику")
        if amount == 0:
            raise ValueError("Неможливо злити 0 кількість води")

        self.current_volume = self.current_volume - amount

    def turn_on(self):
        self.on = True
        self.water_temperature = 100

    def turn_off(self):
        self.on = False
        self.water_temperature = 80

    def status(self):
        print("Об'єм:", self.volume, "\nТемпература:", self.water_temperature, "\nСтан чайника:", self.on,
              "\nПоточний об'єм:", self.current_volume)


try:
    gorenje = Kettle(4, 2)
    gorenje.pour_water(3)
    gorenje.turn_on()
    gorenje.turn_off()
    gorenje.drain_water(1)
    gorenje.status()
except ValueError as e:
    print(f"Помилка: {e}")


class Cloud:
    def __init__(self, square, high, moisture_density):
        if high < 0.5 or high > 15:
            raise ValueError("Неправильне значення. Висота повинна бути від 0.5 до 15 км")
        if square < 1 or square > 10000:
            raise ValueError("Неправильне значення. Площа повинна бути від 1 до 10000 км²")
        if moisture_density < 0 or moisture_density > 30:
            raise ValueError("Неправильне значення. Щільність вологи повинна бути від 0 до 30 г/м³")
        self.square = square
        self.high = high
        self.moisture_density = moisture_density
        self.probability_of_rain = min(moisture_density * 3, 100)

    def increase_moisture_density(self, amount):
        if (self.moisture_density + amount) < 0 or self.moisture_density + amount > 30:
            raise ValueError("Неправильне значення. Щільність вологи повинна бути від 0 до 30 г/м³")
        self.moisture_density = self.moisture_density + amount
        self.probability_of_rain = min(self.moisture_density * 3, 100)

    def rain(self):
        if self.probability_of_rain > 70:
            self.moisture_density = self.moisture_density / 2

    def motion(self, new_high):
        if new_high < 0.5 or new_high > 15:
            raise ValueError("Неправильне значення. Нова висота повинна бути від 0.5 до 15 км")
        self.high = new_high

    def forecast(self):
        print("Висота:", self.high, "\nЩільність вологи:", self.moisture_density, "\nПлощина хмари:", self.square,
              "\nВірогідність дощу:", self.probability_of_rain)


try:
    crying_cloud = Cloud(4, 2, 4)
    crying_cloud.forecast()
    crying_cloud.increase_moisture_density(29)
    crying_cloud.rain()
except ValueError as e:
    print(f"Помилка: {e}")


class Aquarium:
    def __init__(self, length, width, height, water_level, fish_amount, temperature):
        if ((length * width * water_level / 1000) / fish_amount) < 5:
            raise ValueError("Неправильне значення. На кожну рибу потрібно мінімум 5 літрів води")
        if length < 10 or length > 200:
            raise ValueError("Неправильне значення. Довжина повинна бути більше 10 см і менше 200 см")
        if width < 10 or width > 200:
            raise ValueError("Неправильне значення. Ширина повинна бути більше 10 см і менше 200 см")
        if height < 10 or height > 200:
            raise ValueError("Неправильне значення. Висота повинна бути більше 10 см і менше 200 см")
        if water_level < 0 or water_level > height:
            raise ValueError("Неправильне значення. Рівень води не може перевищувати висоту і повинен бути більше 0")
        if temperature < 18 or temperature > 30:
            raise ValueError("Неправильне значення. Температура повинна бути від 18 до 30 °C")
        self.length = length
        self.width = width
        self.height = height
        self.water_level = water_level
        self.fish_amount = fish_amount
        self.temperature = temperature
        self.volume_of_water = length * width * water_level / 1000

    def add_water(self, height_lvl):
        self.water_level = self.water_level + height_lvl

    def add_fish(self):
        if self.volume_of_water / (self.fish_amount + 1) >= 5:
            self.fish_amount = self.fish_amount + 1

    def move_fish(self):
        self.fish_amount = self.fish_amount - 1

    def heat_up_water(self, new_water):
        self.temperature = new_water

    def inspection(self):
        print("Довжина:", self.length, "\nШирина:", self.width, "\nКількість риби", self.fish_amount,
              "\nВисота", self.height, "\nТемпература", self.temperature, "\nОб'єм води", self.volume_of_water)


try:
    my_aquarium = Aquarium(4, 2, 4, 6, 6, 7)
    my_aquarium.add_water(2)
    my_aquarium.heat_up_water(5)
    my_aquarium.add_fish()
    my_aquarium.move_fish()
    my_aquarium.move_fish()
    my_aquarium.inspection()

except ValueError as e:
    print(f"Помилка: {e}")
