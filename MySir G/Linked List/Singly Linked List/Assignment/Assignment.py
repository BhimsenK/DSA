'''1. Defining a Node to describe a node of singly linked list'''


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

        