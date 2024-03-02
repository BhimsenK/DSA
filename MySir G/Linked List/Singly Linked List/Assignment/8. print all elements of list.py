'''8. Define a method to print all the elements of the list.'''


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp != None:
            if temp.item == data:
                return temp
            else:
                temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp != None:
            n = Node(data, temp.next)
            temp.next = n

    '''Simply assign temp variable to the nede referring by start. And using loop, read the values
    until we get temp as None.'''
    def print_list(self):
        temp = self.start
        while temp != None:
            print(temp.item, end=' ')
            temp = temp.next


obj = SLL()
obj.insert_at_start(20)
obj.insert_at_start(10)
obj.insert_at_last(30)
obj.insert_after(obj.search(20), 25)
obj.print_list()

'''OUTPUT : 10 20 25 30 '''
