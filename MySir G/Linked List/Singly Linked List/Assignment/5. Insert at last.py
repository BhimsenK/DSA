'''5. In class SLL, define a method insert_at_last() to insert an element at the end of the list.'''


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

    def insert_at_last(self,data):
        '''Here, if we want to add the node at last what does it mean ?
        It means that out new node should refer to None while the old last node should be refer
        to our new node.
        So thats why, we are first inserting some data into the new node and as if we dont add any value in
        its next, so it means its by default value will be None. So we are not assigning any value to our next.
        '''
        n = Node(data)

        '''here, first we are checking if our Linked List is empty or not. If its not empty then we need to search 
        the last node i.e the node which is refering to None and if its empty then we simply needs to assign the
        new node as a reference in the start/ heads reference of the list.'''
        if not self.is_empty():

            '''If the list is not empty, then we need to search the last node i.e the node which is refering 
            to the None. So we are just taking a node which will refer to the node which is being referred by
            the start/ head.
            So  now both start & temp are refering to the 1st node.
            '''
            temp = self.start

            '''Here, we are just checking if the node which is being referred by the temp is referring to 
            any next node or None. If the node is refering to any node, then we are then assigning the 
            reference of that node in our temp. until we are getting the last node refering to None.'''
            while temp.next is not None:
                temp = temp.next

            '''Once we got the last node, then as I know that last node will be refering to None, so we 
            are simply assigning the reference of that last node from None to our new node. That means, their
            is now only 1 node which is refering to None which is our new node. So it became the last node.'''
            temp.next = n
        else:
            self.start = n


obj = SLL()


