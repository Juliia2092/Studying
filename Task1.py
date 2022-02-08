"""Создайте класс Device, который содержит информацию об устройстве.
С помощью механизма наследования, реализуйте класс
CoffeeMachine (содержит информацию о кофемашине),
класс Blender (содержит информацию о блендере), класс
MeatGrinder (содержит информацию о мясорубке).
Каждый из классов должен содержать необходимые
для работы методы."""


class Device:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.type = kwargs.get('type')
        self.materials = kwargs.get('materials')
        self.size = kwargs.get('size')
        self.volume = kwargs.get('volume')
        self.turns = kwargs.get('turns')


class CoffeeMachine(Device):
    def update_info_coffee_machine(self, **kwargs):
        self.name = kwargs.get('name') if kwargs.get('name') else self.name
        self.type = kwargs.get('type') if kwargs.get('type') else self.type
        self.materials = kwargs.get('materials') if kwargs.get('materials') else self.materials
        self.size = kwargs.get('size') if kwargs.get('size') else self.size
        self.volume = kwargs.get('volume') if kwargs.get('volume') else self.volume
        self.turns = kwargs.get('turns') if kwargs.get('turns') else self.turns

    def __repr__(self):
        return f'Name:{self.name} type:{self.type} materials:{self.materials} size:{self.size} volume:{self.volume} ' \
               f'turns:{self.turns}'


class Blender (Device):
    def update_info_blender(self, **kwargs):
        self.name = kwargs.get('name') if kwargs.get('name') else self.name
        self.type = kwargs.get('type') if kwargs.get('type') else self.type
        self.materials = kwargs.get('materials') if kwargs.get('materials') else self.materials
        self.size = kwargs.get('size') if kwargs.get('size') else self.size
        self.volume = kwargs.get('volume') if kwargs.get('volume') else self.volume
        self.turns = kwargs.get('turns') if kwargs.get('turns') else self.turns

    def __repr__(self):
        return f'Name:{self.name} type:{self.type} materials:{self.materials} size:{self.size} volume:{self.volume} ' \
               f'turns:{self.turns}'


class MeatGrinder(Device):
    def update_info_meat_grinder(self, **kwargs):
        self.name = kwargs.get('name') if kwargs.get('name') else self.name
        self.type = kwargs.get('type') if kwargs.get('type') else self.type
        self.materials = kwargs.get('materials') if kwargs.get('materials') else self.materials
        self.size = kwargs.get('size') if kwargs.get('size') else self.size
        self.volume = kwargs.get('volume') if kwargs.get('volume') else self.volume
        self.turns = kwargs.get('turns') if kwargs.get('turns') else self.turns

    def __repr__(self):
        return f'Name:{self.name} type:{self.type} materials:{self.materials} size:{self.size} volume:{self.volume} ' \
               f'turns:{self.turns}'


coffee_machine = CoffeeMachine(name='Coffee machine', type='Appliances', materials='plastic, stainless steel',
                               size='30x20cm', volume='250ml', turns='1500')

blender = Blender(name='Blender', type='Appliances', materials='plastic, stainless steel', size='50x30cm',
                  volume='1000ml', turns='2500')

meat_grinder = MeatGrinder(name='Meat Grinder', type='Appliances', materials='plastic, stainless steel', size='60x80',
                           volume='5kg', turns='3700')

print(coffee_machine)
print(blender)
print(meat_grinder)

blender.update_info_blender(turns='3000')
print(blender)
