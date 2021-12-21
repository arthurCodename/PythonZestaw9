class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1


    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node
        

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        current = self.head
        prev = current
        while (current.next != None):
            prev = current
            current = current.next
        prev.next = None
        return current

    def merge(self,other):
        if self.is_empty() and other.is_empty():
            return None
        elif self.is_empty():
            self.head = other.head
            self.tail = other.tail
            self.length = other.length
        else:
            self.tail.next = other.head
            self.tail = other.tail
            self.length = self.length + other.length

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.list1, self.list2  = SingleList(), SingleList()
        self.list1.insert_head(Node(1))
        self.list1.insert_head(Node(2))
        self.list1.insert_head(Node(3))
        self.list1.insert_head(Node(4))
        self.list2.insert_head(Node(5))
        self.list2.insert_head(Node(6))
        self.list2.insert_head(Node(7))

    def test_remove_tail(self):
        self.assertEqual(self.list1.remove_tail().data, 1)
        

    def test_merge(self):
        self.list1.merge(self.list2)
        self.assertEqual(self.list1.length, 7)
        self.assertEqual(self.list1.head.data, 4)
        self.assertEqual(self.list1.tail.data, self.list2.tail.data)
       

    def test_clear(self):
        self.list1.clear()
        self.assertEqual(self.list1.head, None)
        self.assertEqual(self.list1.tail, None)
        self.assertEqual(self.list1.length, 0)


if __name__ == '__main__':
    unittest.main()
