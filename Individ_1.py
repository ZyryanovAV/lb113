# Создать класс Payment (зарплата). В классе должны быть представлены поля: фамилия-
# имя-отчество, оклад, год поступления на работу, процент надбавки, подоходный налог,
# количество отработанных дней в месяце, количество рабочих дней в месяце, начисленная и
# удержанная суммы. Реализовать методы:
# вычисления начисленной суммы,
# вычисления удержанной суммы,
# вычисления суммы, выдаваемой на руки,
# вычисления стажа. Стаж вычисляется как полное количество лет, прошедших от года
# поступления на работу, до текущего года.
# Начисления представляют собой сумму, начисленную за отработанные дни, и
# надбавки, то есть доли от первой суммы. Удержания представляют собой отчисления в
# пенсионный фонд (1% от начисленной суммы) и подоходный налог. Подоходный налог
# составляет 13% от начисленной суммы без отчислений в пенсионный фонд.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime


class Payment:

    def __init__(self, Name=' ', oklad=0, year=0, percent=0, Worked_days=0, working_day=1):
        self.__Name = str(Name)
        self.__oklad = int(oklad)
        self.__year = int(year)
        self.__percent = float(percent)
        self.__Worked_days = int(Worked_days)
        self.__working_day = int(working_day)
        self.amount = 0
        self.heldAmount = 0
        self.handAmount = 0
        self.expir= 0

        self.accruedAmount()
        self.withheldAmount()
        self.handedAmount()
        self.experience()

    def accruedAmount(self):
        a = self.__oklad / self.__working_day
        b = a * self.__Worked_days
        percent = self.__percent / 100 + 1
        self.amount = b * percent

    def withheldAmount(self):
        plata = (self.__oklad / self.__working_day) * self.__Worked_days
        self.heldAmount = (plata * 0.13) + (plata * 0.01)

    def handedAmount(self):
        self.handAmount = self.amount - self.heldAmount

    def experience(self):
        self.expir = datetime.now().year - self.__year

    def __round__(self, n=0):
        return round(self.handAmount)

    def __str__(self):
        return f"Опыт работы: {self.expir} год/года/лет \nРасчеты: {self.amount} - {self.heldAmount} = {self.handAmount}"

    def __lt__(self, other):
        return self.__oklad < other.__oklad

    def __eq__(self, other):
        return self.__working_day == other.__working_day

    def __ne__(self, other):
        return self.__percent != other.__percent

    def __gt__(self, other):
        return self.__Worked_days > other.__Worked_days

    def __ge__(self, other):
        return self.expir >= other.expir

    def __le__(self, other):
        return self.handAmount <= other.handAmount

    def __truediv__(self, other):
        if self.__oklad >= other.__oklad:
            return self.__oklad / other.__oklad
        else:
            return other.__oklad / self.__oklad

    def __mul__(self, other):
        return self.__percent * other.__percent

    def __sub__(self, other):
        if self.__Worked_days >= other.__Worked_days:
            return self.__Worked_days - other.__Worked_days
        else:
            return other.__Worked_days - self.__Worked_days

    def __add__(self, other):
        return self.__working_day + other.__working_day


if __name__ == '__main__':
    p_1 = Payment(Name="Михаил", oklad=35000, year=2001, percent=15, Worked_days=20, working_day=24)
    p_2 = Payment(Name="Иван", oklad=35000, year=2003, percent=10, Worked_days=23, working_day=24)

    print(f"{p_1}")
    print(f"Выданная сумма: {round(p_1)}\n")

    print(f"oklad_1 < oklad_2: {p_1 < p_2}")
    print(f"workingDays1 > workingDays2: {p_1 > p_2}")
    print(f"percent_1 != percent_2: {p_1 != p_2}")
    print(f"daysWorked_1 == daysWorked_2: {p_1 == p_2}")
    print(f"Experience_1 >= Experience_2: {p_1 >= p_2}")
    print(f"handAmount_1 <= handAmount_2: {p_1 <= p_2}\n")

    print(f"Разница в заработной плате: {p_1 / p_2}")
    print(f"Произведение процентов: {p_1 * p_2}")
    print(f"Добавленные рабочие дни: {p_1 + p_2}")
    print(f"Разница в отработанных днях: {p_1 - p_2}")