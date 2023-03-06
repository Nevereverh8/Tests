class DLinkedList:
    head = None
    tail = None
    ptr = None

    class Node:
        def __init__(self, data, left=None, right=None):
            self.left = left
            self.right = right
            self.data = data

    def push(self, data):
        if self.tail:
            self.ptr = self.tail
            self.tail = self.Node(data, self.ptr)
            self.ptr.right = self.tail
        else:
            self.tail = self.Node(data)
            self.head = self.tail

    def unshift(self, data):
        if self.head:
            self.ptr = self.head
            self.head = self.Node(data, None, self.ptr)
            self.ptr.left = self.head
        else:
            self.head = self.Node(data)
            self.tail = self.tail

    def pop(self):
        if self.tail and self.tail.left:
            self.tail = self.tail.left
            self.tail.right = None
        elif self.tail:
            del self.tail
            self.tail = None
            self.head = None

    def shift(self):
        if self.head and self.head.right:
            self.head = self.head.right
            self.head.left = None
        elif self.head:
            del self.head
            self.head = None
            self.tail = None

    def out(self):
        if self.head:
            node = self.head
            while node.right:
                print(node.data, end=' ')
                node = node.right
            print(node.data)
        else:
            print('Empty double linked list')


a = DLinkedList()
