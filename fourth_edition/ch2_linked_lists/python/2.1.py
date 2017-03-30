'''
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
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

dup_data = dict()


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        # print(data, " inserted!")

    def traversal(self):
        curr_node = self.head
        while curr_node:
            data_ = curr_node.get_data()
            print(data_, end=" ")
            curr_node = curr_node.get_next_node()
        print("")

    def build_dup_hashset(self):
        global dup_data
        curr_node = self.head
        while curr_node:
            data_ = curr_node.get_data()
            if data_ in dup_data:
                count = dup_data[data_]
                dup_data[data_] = count + 1
            else:
                dup_data[data_] = 1
            curr_node = curr_node.get_next_node()

    def del_node(self, data):
        curr_node = self.head
        prev_node = None

        while curr_node:
            if curr_node.get_data() == data:
                if prev_node:
                    prev_node.set_next_node(curr_node.get_next_node())
                else:
                    self.head = curr_node.get_next_node()
                print(data, " deleted!")
                return
            else:
                prev_node = curr_node
                curr_node = curr_node.get_next_node()

    def del_dups(self):
        global dup_data
        self.build_dup_hashset()
        for k, v in dup_data.items():
            if v > 1:
                for _ in range(v-1):
                    self.del_node(k)
                    dup_data[k] = v - 1


myLL = LinkedList()

print("Inserting nodes to linked list")
myLL.insert_node(10)
myLL.insert_node(20)
myLL.insert_node(50)
myLL.insert_node(30)
myLL.insert_node(20)
myLL.insert_node(50)
myLL.insert_node(50)
myLL.insert_node(20)
myLL.insert_node(10)
myLL.insert_node(60)

print("Traversing the linked list")
myLL.traversal()

print("Deleting duplicate data")
print(myLL.del_dups())

print("Traversing the de-duplicated linked list")
myLL.traversal()
