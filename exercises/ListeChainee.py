__author__ = 'PWXG8293'
from Cell import *


class ListeChainee:
    def __init__(self):
        self.head = None
        self.tail = None

    def addHead(self, value):
        print("adding value", value, " at the head of the list")
        cell = Cell()
        cell.value = value
        cell.previous = None
        if self.head == None:
            cell.next = None
            self.head = cell
            self.tail = cell
        else:
            cell.next = self.head
            self.head.previous = cell
            self.head = cell
        self.dump()


    def dump(self):
        print("L[]= "),
        ptr = self.head
        while ptr is not None and ptr.next is not None:
            print (ptr.value),
            ptr = ptr.next
        if self.tail is not None:
            print(self.tail.value)  # on affiche le dernier element car la valeur de son next est None

    def removeHead(self):
        if self.head == None:
            print (" La liste est vide, impossible de supprimer le premier element")
            return -1
        elif self.head.next == None:
            value = self.head.value
            self.head = None
            self.tail = None
            self.dump()
            return value
        else:
            # verifier qu'on a plus d'un element avant de proceder a la supression
            value = self.head.value
            self.head.next.previous = None
            self.head = self.head.next
            self.dump()
            return value

    def removeTail(self):
        if self.tail == None:
            print (" La liste est vide, impossible de supprimer le dernier element")
            return -1
        elif self.tail.previous == None:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.dump()
            return value
        else:
            # verifier qu'on a plus d'un element avant de proceder a la supression
            value = self.tail.value
            self.tail.previous.next = None
            self.tail = self.tail.previous
            self.dump()
            return value

    def addTail(self, v):
        print("adding value", v, " at the end of the list")
        cell = Cell()
        cell.value = v
        cell.next = None
        if self.tail == None:
            cell.previous = None
            self.head = cell
            self.tail = cell
        else:
            cell.previous = self.tail
            self.tail.next = cell
            self.tail = cell
        self.dump()


    def find(self, value):
        ptr = self.head
        while ptr is not None and ptr.next is not None:
            if ptr.value == value:
                print("Trouve!!", value)
                return True
                break;
            ptr = ptr.next
        return False

    def contains(self, item):
        return self.find(item)