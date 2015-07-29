__author__ = 'PWXG8293'


class Cell:
    def __init__(self):
        self.value = None
        self.previous = None
        self.next = None

    def getValue(self):
        return self.value

    def dump(self):
        print("Value: ", self.value, "Previous:", self.previous, "Next: ", self.next)
