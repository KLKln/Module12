"""
Program: abstract_class.py
Author:  Kelly Klein
Date: 07/15/2020

This program creates an abstract class method called Rider
    then creates three subclasses that return a statement
    about how it rides and how many riders
"""

from abc import ABC, abstractmethod


class Rider(ABC):

    @abstractmethod
    def ride(self):
        pass

    def riders(self):
        pass


class Bicycle(Rider):

    def __init__(self):
        self.ride = 'Human powered, not enclosed'
        self.riders = '1 or 2 if tandem or a daredevil'

    def ride(self):
        return self.ride

    def riders(self):
        return self.riders


class Motorcycle(Rider):
    def __init__(self):
        self.ride = 'Engine powered, not enclosed'
        self.riders = '1 or 2, maybe 3 with a sidecar'

    def ride(self):
        return print(self.ride)

    def riders(self):
        return print(self.riders)


class Car(Rider):
    def __init__(self):
        self.ride = 'Engine powered, enclosed'
        self.riders = '1 plus comfortably'

    def ride(self):
        return self.ride

    def riders(self):
        return self.riders


if __name__ == '__main__':
    b = Bicycle()
    print(str(b.ride))
    print(str(b.riders))

    m = Motorcycle()
    print(str(m.ride))
    print(str(m.riders))

    c = Car()
    print(str(c.ride))
    print(str(c.riders))


