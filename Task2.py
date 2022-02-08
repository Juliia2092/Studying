"""Создайте класс Ship, который содержит информацию
о корабле.
С помощью механизма наследования, реализуйте
класс Frigate (содержит информацию о фрегате), класс
Destroyer (содержит информацию об эсминце), класс
Cruiser (содержит информацию о крейсере).
Каждый из классов должен содержать необходимые
для работы методы."""


class Ship:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.type = kwargs.get('type')
        self.size = kwargs.get('size')
        self.volume = kwargs.get('volume')
        self.speed = kwargs.get('speed')
        self.distance = kwargs.get('distance')


class Frigate(Ship):
    def update_info_frigate(self, **kwargs):
        self.name = kwargs.get('name') if kwargs.get('name') else self.name
        self.type = kwargs.get('type') if kwargs.get('type') else self.type
        self.size = kwargs.get('size') if kwargs.get('size') else self.size
        self.volume = kwargs.get('volume') if kwargs.get('volume') else self.volume
        self.speed = kwargs.get('speed') if kwargs.get('speed') else self.speed
        self.distance = kwargs.get('distance') if kwargs.get('distance') else self.distance

    def __repr__(self):
        return f'Name:{self.name} type:{self.type} size:{self.size} volume:{self.volume} speed:{self.speed} ' \
               f'distance:{self.distance}'


class Destroyer(Ship):
    def update_info_destroyer(self, **kwargs):
        self.name = kwargs.get('name') if kwargs.get('name') else self.name
        self.type = kwargs.get('type') if kwargs.get('type') else self.type
        self.size = kwargs.get('size') if kwargs.get('size') else self.size
        self.volume = kwargs.get('volume') if kwargs.get('volume') else self.volume
        self.speed = kwargs.get('speed') if kwargs.get('speed') else self.speed
        self.distance = kwargs.get('distance') if kwargs.get('distance') else self.distance

    def __repr__(self):
        return f'Name:{self.name} type:{self.type}  size:{self.size} volume:{self.volume} speed:{self.speed} ' \
               f'distance:{self.distance} '


class Cruiser(Ship):
    def update_info_cruiser(self, **kwargs):
        self.name = kwargs.get('name') if kwargs.get('name') else self.name
        self.type = kwargs.get('type') if kwargs.get('type') else self.type
        self.size = kwargs.get('size') if kwargs.get('size') else self.size
        self.volume = kwargs.get('volume') if kwargs.get('volume') else self.volume
        self.speed = kwargs.get('speed') if kwargs.get('speed') else self.speed
        self.distance = kwargs.get('distance') if kwargs.get('distance') else self.distance

    def __repr__(self):
        return f'Name:{self.name} type:{self.type} size:{self.size} volume:{self.volume} speed:{self.speed} ' \
               f'distance:{self.distance}'


frigate = Frigate(name='Frigate', type='warship', size='124,8х15,2х4,2m', volume='4035', speed='30/14',
                  distance='4850')

destroyer = Destroyer(name='Destroyer', type='warship', size='156x17,2x8,2', volume='6500', speed='33.4',
                      distance='4500')

cruiser = Cruiser(name='Cruiser', type='ship', size='251x28,5x10,33 ', volume='24500', speed='31',
                  distance='5000')

print(frigate)
print(destroyer)
print(cruiser)

cruiser.update_info_cruiser(type='warship', distance='4300')
print(cruiser)
