class Node():

    def __init__(self, data):

        self.data = data
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList():

    def __init__(self):

        self.head = None
        self.tail = None
        self.numberOfNodes = 0

    def insert_end(self, data):
        '''This operations inserts at the end of the linkedList, that is we manipulate the tail node in o(1)'''
        new_node = Node(data)

        # When the list is empty
        if self.head is None:
            # This means head node is the only node in the linked list
            self.head = new_node
            self.tail = new_node

        # There is atleast one item in the data structure
        # We keep inserting item at the end
        else:
            new_node.previous_node = self.tail
            # update tail node to current new node
            self.tail.next_node = new_node
            # add new node as new terminal node
            self.tail = new_node

    # we can traverse in both the direction
    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:

            print(actual_node.data)
            actual_node = actual_node.next_node

    def traverse_backward(self):

        actual_node = self.tail

        while actual_node is not None:

            print(actual_node.data)
            actual_node = actual_node.previous_node


if __name__ == '__main__':

    linkedList = DoublyLinkedList()
    linkedList.insert_end(1)
    linkedList.insert_end(2)
    linkedList.insert_end(3)

    linkedList.traverse_forward()
    print("------------------")
    linkedList.traverse_backward()
