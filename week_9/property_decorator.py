class Celsius:
    def __init__(self):
        self.__temperature = 0

    def to_fahrenheit(self):
        return self.__temperature * 1.8 + 32

    @property    
    def temperature(self):
        print('Getting value...')
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):
        print('setting value...')
        if value < -273:
            print("Temperature is out of range!")
        else:
            self.__temperature = value

    # using property object
    # temperature = property(get_temperature, set_temperature)

human = Celsius()
print(1)
print(human.temperature)
human.temperature = 300
human.temperature = -300
print(human.to_fahrenheit())

print(human.temperature)
