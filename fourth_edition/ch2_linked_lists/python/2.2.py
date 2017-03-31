'''
Implement an algorithm to find the nth to last element of a singly linked list.
'''


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data=None):
        new_node = Node(data, self.head)
        self.head = new_node

    def find_nth_to_last__node(self, data=None):
        curr_node = self.head
        while curr_node:
            if curr_node.get_data() == data:
                print(data, end=" ")
                next_node = curr_node.get_next_node()
                while next_node:
                    print(next_node.get_data(), end=" ")
                    next_node = next_node.get_next_node()
                break
            curr_node = curr_node.get_next_node()
        else:
            print(data, "not present")
        print(" ")


myLL = LinkedList()
myLL.insert_node(10)
myLL.insert_node(20)
myLL.insert_node(30)
myLL.insert_node(40)
myLL.insert_node(50)
myLL.insert_node(60)
myLL.insert_node(70)
myLL.insert_node(80)

myLL.find_nth_to_last__node(50)
myLL.find_nth_to_last__node(90)
