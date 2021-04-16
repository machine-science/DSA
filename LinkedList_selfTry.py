class Node():

    def __init__(self, data):

        self.data = data
        self.next_node = None

class LinkedList():

    def __init__(self):

        self.head = None
        self.number_of_nodes = 0

    # In linked list we can either add at the beginnig or at the end

    def insert_beginning(self, data):

        self.number_of_nodes = self.number_of_nodes + 1

        new_node = Node(data)

        if self.head is None:
            print("Head is Null")
            print("Adding {0} to first node".format(data))
            self.head = new_node

        else:
            print("currently head is {}".format(self.head.data))
            new_node.next_node = self.head
            self.head = new_node
            
            print(self.head.data)
            print(self.head.next_node.next_node)

ll = LinkedList()

ll.insert_beginning(10)
ll.insert_beginning(20)
