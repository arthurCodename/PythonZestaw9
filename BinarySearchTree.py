class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if node.data < self.data:   # mniejsze na lewo
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:   # większe lub równe na prawo
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None

    def remove(self, data):  # self na pewno istnieje
        # Są lepsze sposoby na usuwanie.
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
        elif self.data < data:
            if self.right:
                self.right = self.right.remove(data)
        else:                # self.data == data
            if self.left is None:   # przeskakuje self
                return self.right
            else:     # self.left na pewno niepuste
                # Szukamy największego w lewym poddrzewie.
                node = self.left
                while node.right:   # schodzimy w dół
                    node = node.right
                node.right = self.right   # przyczepiamy
                return self.left
        return self
        
    @staticmethod
    def count_leafs(top):
        if top is None:
            return 0
        if (top.left is None and top.left is None):
            return 1
        else: 
            return Node.count_leafs(top.left) + Node.count_leafs(top.right)

    @staticmethod
    def count_total(top):
        if top is None:
            return 0
        else:
            return top.data + Node.count_total(top.left) + Node.count_total(top.right)





import unittest 

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        

    def test__count_leaf(self):
        
        self.assertEqual(Node.count_leafs(self.root), 3)

    def test__count_leaf(self):
        
        self.assertEqual(Node.count_total(self.root), 15)   

    def tearDown(self): pass 

if __name__ == '__main__':
    unittest.main()


