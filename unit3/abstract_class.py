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
        return str(self.ride)

    def riders(self):
        return str(self.riders)


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
    Bicycle.ride
