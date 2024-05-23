#https://pastebin.com/ZG1AbunX
#Array implementation of Queues
#Leetcode(994)
def enQueue(Q, ele):
    Q.append(ele)
    print(ele, " enqueued successfully")


def deQueue(Q):
    if len(Q) == 0:
        print("Queue is empty")
        return
    print(Q[0], " element is getting deleted")
    Q.pop(0)

Q = []
enQueue(Q, 10)
enQueue(Q, 20)
enQueue(Q, 30)
enQueue(Q, 40)
print(Q)

deQueue(Q)
print(Q)

deQueue(Q)
print(Q)

deQueue(Q)
print(Q)

deQueue(Q)
print(Q)

deQueue(Q)
print(Q)

# Output:

# 10  enqueued successfully
# 20  enqueued successfully
# 30  enqueued successfully
# 40  enqueued successfully
# [10, 20, 30, 40]
# 10  element is getting deleted
# [20, 30, 40]
# 20  element is getting deleted
# [30, 40]
# 30  element is getting deleted
# [40]
# 40  element is getting deleted
# []
# Queue is empty
# []
