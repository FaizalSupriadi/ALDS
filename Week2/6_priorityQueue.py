class priorityQueue:
	def __init__(self):
		self.queue = []
	
	def Queue( self, data, priority ):
		self.queue.append([data,priority])
		
	def Dequeue(self):
		maximum = [0,0]
		for i in range(0, len(self.queue)):
			if maximum[1] < self.queue[i][1]:
				maximum = self.queue[i]
		self.queue.remove(maximum)
		return maximum[0]
	
	def Contains(self, data):
		for i in range(0, len(self.queue)):
			if data == self.queue[i][0]:
				return True
		return False
	
	def Remove(self, data):
		memo =[]
		for i in range(0, len(self.queue)):
			if data == self.queue[i][0]:
				memo.append(self.queue[i])
		for j in range(0, len(memo)):
			self.queue.remove(memo[j])
		
	def see(self):
		print(self.queue)
				
a = priorityQueue()

a.Queue(1, 6)
a.Queue(4, 1)
a.Queue(7, 2)
a.Queue(7, 4)
print(a.Dequeue())
a.see()
print(a.Contains(4))
print(a.Contains(3))
a.Remove(7)
a.Remove(8)
a.see()