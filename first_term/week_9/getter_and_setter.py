class Celsius:
    def __init__(self):
        self.__temperature = 0

    def to_fahrenheit(self):
        return self.__temperature * 1.8 + 32
            
    def get_temperature(self):
        print('Getting value...')
        return self.__temperature
    
    def set_temperature(self, value):
        if value < -273:
            print("Temperature is out of range!")
        else:
            self.__temperature = value

    # using property object
    temperature = property(get_temperature, set_temperature)

human = Celsius()
print(1)
human.set_temperature(300)
human.set_temperature(-300)
print(human.get_temperature())
print(human.to_fahrenheit())

print(human.temperature)
