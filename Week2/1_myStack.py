class myStack:
	"""
	Parameters
	----------
	val: int
		val is an int
		
	Returns
	-------
	tmp : int
		return the popped value
	self.stack[len(self.stack)-1] : int
		return the value last in the array
	"""
	def __init__(self):
		self.stack = []
		
	def push(self, val):
		self.stack.append(val)
	
	def pop(self):
		tmp = self.stack[len(self.stack)-1]
		self.stack.remove(self.stack[len(self.stack)-1])
		return tmp
	
	def peek(self):
		return self.stack[len(self.stack)-1]
	
	def isEmpty(self):
		if self.stack == []:
			return 1
		return 0

stack = myStack()

print(stack.isEmpty())
for i in range(1,5):
	stack.push(i)
print(stack.isEmpty())
for i in range(0,4):
	print(stack.peek())
	print(stack.pop())
	print(stack.isEmpty())