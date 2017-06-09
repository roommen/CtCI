'''
Implement a MyQueue class which implements a queue using two stacks.
'''


stack1 = list()
stack2 = list()
max_ = 10


class MyQueue(object):
    def push(self, val):
        global stack1, stack2
        if len(stack1) == max_:
            if len(stack2) == 0:
                for x in stack1[::-1]:
                    stack2.append(x)
                stack1 = []
            else:
                return "Queue Full!"
        stack1.append(val)

    def pop(self):
        global stack1, stack2
        if len(stack2) == 0:
            if len(stack1) > 0:
                stack2 = stack1
                stack1 = []
            else:
                return "Queue Empty"
        return stack2.pop(-1)

    def queue(self, val):
        # Call the push
        global stack1, stack2
        self.push(val)
        # print(stack1, stack2)

    def dequeue(self):
        # Call the pop
        global stack1, stack2
        pop_out = self.pop()
        # print(stack1, stack2)
        return pop_out

mq = MyQueue()


mq.queue(10)
mq.queue(20)
mq.queue(30)
mq.queue(40)
mq.queue(50)
mq.queue(60)
mq.queue(70)
mq.queue(80)
mq.queue(90)
mq.queue(100)
mq.queue(110)
mq.queue(120)
mq.queue(130)

print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())

mq.queue(140)

print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())

mq.queue(150)

