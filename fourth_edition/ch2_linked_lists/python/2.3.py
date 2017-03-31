'''
Implement an algorithm to delete a node in the middle of a single linked list, given
only access to that node.
EXAMPLE
Input: the node ‘c’ from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a->b->d->e
'''


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data=None):
        self.data = data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node=None):
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data=None):
        new_node = Node(data, self.head)
        self.head = new_node

    def traversal(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.get_data(), end=" ")
            curr_node = curr_node.get_next_node()
        print("")

    def del_node(self, data=None):
        curr_node = self.head
        prev_node = None
        while curr_node:
            if curr_node.get_data() == data:
                if prev_node:
                    prev_node.set_next_node(curr_node.get_next_node())
                else:
                    self.head = curr_node.get_next_node()
                break
            else:
                prev_node = curr_node
                curr_node = curr_node.get_next_node()


myLL = LinkedList()
myLL.insert_node('e')
myLL.insert_node('d')
myLL.insert_node('c')
myLL.insert_node('b')
myLL.insert_node('a')

myLL.traversal()

myLL.del_node('c')

myLL.traversal()
