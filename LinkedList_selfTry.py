class Node():

    def __init__(self, data):

        self.data = data
        self.next_node = None


class LinkedList():

    def __init__(self):

        self.head = None
        self.numberOfNodes = 0

    def insert_start(self, data):
        # increase the number of nodes
        self.numberOfNodes = self.numberOfNodes + 1
        # initialize the new node with data and pointer to next node
        new_node = Node(data)
        '''
        Now I will check if the header is already initialized, if not then the new node is the header node
        else, we need to add the new node as the new header anc change the nexnode pointer to current header
        '''
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):

        self.numberOfNodes = self.numberOfNodes + 1

        new_node = Node(data)

        actual_head_node = self.head

        while actual_head_node.next_node is not None:
            actual_head_node = actual_head_node.next_node

        actual_head_node.next_node = new_node

    def remove(self, data):

        if self.head is None:
            ''' This checks if the LinkedList is empty'''
            print("First check")
            return

        actual_node = self.head
        previousNode = None

        while actual_node is not None and actual_node.data != data:
            previousNode = actual_node
            actual_node = actual_node.next_node

        # Search Miss - Means element is not in list
        if actual_node is None:
            return

        self.numberOfNodes = self.numberOfNodes - 1

        if previousNode is None:
            ''' Here we are reinitializing '''
            self.head = actual_node.next_node
        else:
            previousNode.next_node = actual_node.next_node

    def size_of_list(self):
        return self.numberOfNodes

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node


linkedList = LinkedList()
linkedList.insert_start(10)
linkedList.insert_start(9)
linkedList.insert_start(8)
print(linkedList.size_of_list())
linkedList.traverse()
print("---------------------")
linkedList.remove(9)
print(linkedList.size_of_list())
linkedList.traverse()
