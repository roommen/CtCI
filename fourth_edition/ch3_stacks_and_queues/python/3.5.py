'''
Implement a MyQueue class which implements a queue using two stacks.
'''


stack1 = list()
stack2 = list()
max_ = 10


def push(val):
    global stack1, stack2
    if len(stack1) == max_:
        if len(stack2) == 0:
            for x in stack1[::-1]:
                stack2.append(x)
            stack1 = []
        else:
            return "Queue Full!"
    stack1.append(val)


def pop():
    global stack1, stack2
    if len(stack2) == 0:
        if len(stack1) > 0:
            stack2 = stack1
            stack1 = []
        else:
            return "Queue Empty"
    return stack2.pop(-1)


def queue(val):
    # Call the push
    global stack1, stack2
    push(val)
    # print(stack1, stack2)


def dequeue():
    # Call the pop
    global stack1, stack2
    pop_out = pop()
    # print(stack1, stack2)
    return pop_out


queue(10)
queue(20)
queue(30)
queue(40)
queue(50)
queue(60)
queue(70)
queue(80)
queue(90)
queue(100)
queue(110)
queue(120)
queue(130)

print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())

queue(140)

print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())

queue(150)



