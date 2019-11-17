class myStack:
	
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
	stack = myStack()
	for i in range(0, len(val)):
		if val[i] == '[' or val[i] == '(' or val[i] == '<':
			stack.push(val[i])
		if val[i] == ']' and stack.peek() == '[' or val[i] == ')' and stack.peek() == '(' or val[i] == '>'and stack.peek() == '<':	
			stack.pop()
	return stack.isEmpty()

bracket = "(<>)[]()(()())"
print(valid_bracket(bracket))


