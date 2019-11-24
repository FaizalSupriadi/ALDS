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
	
def valid_bracket(val):
	"""
	Parameters
	----------
	val: string
		val is a string with given brackets
		
	Returns
	-------
	stack.isEmpty() : function
		this will return whether the stack is empty or not via a bool
	"""
	stack = myStack()
	for i in range(0, len(val)):
		if val[i] == '[' or val[i] == '(' or val[i] == '<':
			stack.push(val[i])
		if val[i] == ']' and stack.peek() == '[' or val[i] == ')' and stack.peek() == '(' or val[i] == '>'and stack.peek() == '<':	
			stack.pop()
	return stack.isEmpty()

bracket = "(<>)[]()(()())"
print(valid_bracket(bracket))


