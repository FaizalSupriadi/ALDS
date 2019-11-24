
class linkedList:

	"""
	Parameters
	----------
	data:int
		data is an int if filled or None if linkedList is called without one
	value:int
		value is an int that is added to the list
	Returns
	-------
	self.value : int
		return the current value in the list
	"""
	def __init__(self, data=None):
		self.value  = data
		self.tail = None
		
	def append(self,value):
		if self.value == None:
			self.value = value
			return
		if self.tail == None:
			self.tail = linkedList(value)
			return	
		self.tail.append(value)
		
	def delete(self, value):
		if self.tail == None:
			return
		if self.value == value:
			self.value = self.tail.value
			self.tail = self.tail.tail
		self.tail.delete(value)
		
	def min(self):
		if self.tail != None:
			return self.value
		if self.tail.min() < self.value:
			return self.tail.min()
		return self.value
		
		
	def see(self):
		prints = self.tail
		print(self.value)
		while( prints != None):
			print(prints.value)
			prints = prints.tail

a = linkedList()

a.append(4)
a.append(5)
a.append(6)
a.see()
a.delete(4)
a.append(8)
print("-----\n",a.min(),"\n-----")
a.see()
