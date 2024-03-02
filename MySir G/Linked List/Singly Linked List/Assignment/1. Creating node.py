'''1. Defining a Node to describe a node of singly linked list'''


class Node:

    '''this is a constructor. Imagin there are 2 boxes inside a Single big box.
    Now, suppose those 2 boxes are item, next. (Item : Data, Next : reference of next node).
    Here, these 2 boxes will be inside a node.
    So basically, for creating a node we first need to have item, reference variable inside it.
    Here, we are keeping it as None until we get some input for them.'''
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next




