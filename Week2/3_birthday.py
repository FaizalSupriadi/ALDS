import random

def birthday(val):
	"""
	Parameters
	----------
	val: int
		val is the amount of students
	Returns
	-------
	same/100 : float
		return the amount of how many times people had the same birthday
	"""
	days =[]
	same=0
	for i in range(0,100):
		for j in range(0,val):
			days.append(random.randrange(1,356))
		for k in range(0, len(days)):
			for l in range(k+1, len(days)): 
				if days[k] == days[l]:
					same+=1
	return same/100

print(birthday(2))