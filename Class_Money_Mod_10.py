"""Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
поле для хранения копеек (центы, евроценты, копейки
и т.д.).
Реализовать методы для вывода суммы на экран, задания значений для частей. """


class Money:
    def __init__(self, currency, whole, rest):
        self.__currency = currency
        self.__whole = whole
        self.__rest = rest

    def get_whole(self):
        return self.__whole

    def set_whole(self, whole):
        self.__whole = whole

    def get_rest(self):
        return self.__rest

    def set_rest(self, rest):
        self.__rest = rest

    def __add__(self, other):
        return (self.__whole, self.__rest) + other.whole

    def __repr__(self):
        return f'Currency: {self.__currency}, whole: {self.__whole}, rest:{self.__rest}'


payment_account = Money(currency='UAH', whole=14251, rest=20)

print(payment_account)










