'''4. In class SLL, define a method insert_at_start() to insert an element at the starting of the list.'''


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
        '''Suppose, we need to add new node in SLL, then whats the first thing we should be having ?
        Its that we should have that new node created. So simply we are creating a new node by creating
        an object of the class Node.
        Here, after creating a node, bydefault it will assign the item & next as None. So we have to pass
        the data as in the Node class, in the  constructor we are assigning default values as None so.'''
        n = Node(data, self.start)
        '''item : will be the data which user will pass.
        next    : If we want to add the data in first position, then inside the next variable we should save 
        the reference of older 1st node which was saved in start. 
        So we are simply assigning that starts reference into this new nodes reference. Now both start and new node
        are referring to the old 1st node.'''

        self.start = n
        '''Here, if we want to add this new node @1st position, then what we required ?
        we requried that the Start should be refering to this new node instead of old 1st node.
        So we are assigning this new nodes object inside the start. 
        So now start is referring to this node, and this node is referring to old 1st node which is now 2nd.'''
obj = SLL()


