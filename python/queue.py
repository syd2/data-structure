class Queue():

    def __init__(self):
        self.items = []
    
    def Enqueue(self, data):
        self.items.append(data)

    def Dequeue(self):
        self.items.pop(0)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

q1 = Queue()
for i in range(10):
    q1.Enqueue(i)
print(q1.items)
q1.Dequeue()
q1.Dequeue()
print(q1.items)
q1.Enqueue(10)
print(q1.items)
q1.Dequeue()
print(q1.items)