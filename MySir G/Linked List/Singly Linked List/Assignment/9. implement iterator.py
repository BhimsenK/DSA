'''9. Implement iterator for SLL to access all the elements of the list in a sequence.'''

#on hold

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


    def print_list(self):
        temp = self.start
        while temp != None:
            print(temp.item, end=' ')
            temp = temp.next

    def __iter__(self):
        return SLL_Iteratore(self.start)

class SLL_Iteratore:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

obj = SLL()
obj.insert_at_start(20)
obj.insert_at_start(10)
obj.insert_at_last(30)
obj.insert_after(obj.search(20), 25)
obj.print_list()
print()


for i in obj:
    print(i)


