
class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:

    def __init__(self):
        # Initially first node/head value is null because the linked list is empty
        self.head = None
        # At the beginning number of noder is 0. Which means there ios no item in the linked list datastructure
        self.numofNodes = 0  

    def insert_start(self, data):
        """ This method is going to get data and insert it into the linked list. Time complexity is O(1)"""

        # We will first increment the number of nodes
        self.numofNodes = self.numofNodes + 1
        
        # Then we instantiate the new node
        new_node = Node(data)

        # We need to check if this is the first node of the linked list or not that is if [head node is null or not]
        if not self.head:
            self.head = new_node
        else:
            # If head node is not empty,
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self, data):

        # We will first increment the number of nodes
        self.numofNodes = self.numofNodes + 1

        new_node = Node(data)

        actual_node = self.head # Pointing to the Fist node of the linked list

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode
        
        actual_node.nextNode = new_node

    def remove(self, data):

        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while ((actual_node is not None) and (actual_node.data != data)):
            previous_node = actual_node
            actual_node = actual_node.nextNode

        # This is a search miss, that is the item is not present in the linked list
        if actual_node is None:
            return

        self.numofNodes = self.numofNodes - 1

        if previous_node is None:
            self.head = actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode


    def siz_of_list(self):
        return self.numofNodes

    def traverse(self):

        actual_node = self.head

        # while we are not at the end of the list
        # We will print the actual node
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

linked_list = LinkedList()
linked_list.insert_start(10)
linked_list.insert_start(5)
linked_list.insert_start(3)
linked_list.insert_end(3)
linked_list.traverse()
print(linked_list.siz_of_list())
print("----------------")        

linked_list.remove(3)
linked_list.traverse()
print(linked_list.siz_of_list())