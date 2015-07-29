__author__ = 'PWXG8293'


class Element:
    def __init__(self):
        self.value = None
        self.next = None


class Liste:
    def __init__(self):
        self.first = None


def append(self, value):
    element = Element()
    element.value = value
    element.next = None
    if self.first is None:
        self.first = element
    else:
        ptr = self.first
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = element