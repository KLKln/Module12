from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Abstract method not implemented")


class InvalidSideError(Exception):
    pass


#@Shape.register
class Rectangle(Shape):
    def __init__(self, h, b):
        if h <= 0:
            raise InvalidSideError('Value cannot be negative')
        else:
            self.height = h
        if b <= 0:
            raise InvalidSideError('Value cannot be negative')
        else:
            self.base = b

    def area(self):
        return self.height*self.base
