'''3. Define a method is_empty() to check if the linked list is empty is SLL class'''


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    '''Here we are defining a function for checking if the linked list is empty or not.
    Logic : we are just checking that if start is refering to None, it means its empty.'''
    def is_empty(self):
        return self.start == None


obj = SLL()
empty = obj.is_empty() #as this function will be returning something so we need to save the output first inside any variable.
print(empty)


