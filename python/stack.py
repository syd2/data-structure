class Stack():

	def __init__(self):
		self.items = []
		self.len = 0
	def push(self, data):
		self.items.append(data)
		self.len += 1
	def pop(self):
		self.items.pop()
		self.len -= 1
	def isEmpty(self):
		if self.items == []:
			return True
		else:
			return False

s1 = Stack()
for i in range(20):
	s1.push(i)
print(s1.items)
s1.pop()
print(s1.items)
print(s1.isEmpty())
print(s1.len)
