import random
def partition(a, lo, hi):
	"""
	Parameters
	----------
	a: list
		list with values
	lo:int
		lo has the lowest indnex of the list
	hi:int
		hi has the highest index of the list
	Returns
	-------
	i : int
		return i, i has the next index to use for hi
	count : int
		count has counted how many times values are compared
	"""
	pivot = a[hi]
	i=lo
	count = 0
	for j in range(lo,hi):
		count += 1
		if a[j] <= pivot:
			a[i], a[j] = a[j], a[i] 
			i+=1
	a[i], a[hi] = a[hi], a[i] 
	
	return i, count

def quickSort(a, lo, hi):
	"""
	Parameters
	----------
	a: list
		list with values
	lo:int
		lo has the lowest indnex of the list
	hi:int
		hi has the highest index of the list
	Returns
	-------
	a : list
		return the list
	count : int
		count has counted how many times values are compared
	"""
	count = [[],[],[]]
	if lo >= hi:		
		return a, 1
	p, count[0]= partition(a,lo,hi )
	a, count[1] = quickSort(a, lo, p-1, )
	a, count[2] = quickSort(a, p+1, hi, )
	return a, sum(count)+1

for i in range(0, 100):
	a = []
	for j in range(0,10):
		a.append( random.randrange(1,100))
	print(quickSort(a, 0, len(a)-1 ))
