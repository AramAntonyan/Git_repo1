class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def sedan(self):
        return "This car is a sedan"

    def sport_car(self):
        return "This is a sport car."


car1 = Car('Honda', 'Civic', 2010)
print(car1.make)
print(car1.model)
print(car1.year)
print(car1.sedan())

car2 = Car('Nissan', '370Z', 2022)
print(car2.make)
print(car2.sport_car())


class Electric_car(Car):
    def __init__(self, make, model, year, battery):
        super().__init__(make, model, year)
        self.battery = battery

    def rear_motor(self):
        return "This car has a rear motor"

    def red_color(self):
        return "Red color."

car3 = Electric_car('Tesla', 'Model 3', 2021, '271 hp')
print(car3.make)
print(car3.battery)
print(car3.sedan())
print(car3.rear_motor())
print(car3.red_color())

