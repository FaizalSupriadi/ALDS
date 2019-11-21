import random
def median(array):
	length = len(array)
	return array[int(length/2)]
		

def partition(a, lo, hi):

	pivot = median(a[lo:hi+1])
	
	index = a.index(pivot)

	a[hi], a[index] = a[index], a[hi]
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
	count = [[],[],[]]
	if lo >= hi:		
		return a, 1
	p, count[0]= partition(a,lo,hi )
	a, count[1] = quickSort(a, lo, p-1, )
	a, count[2] = quickSort(a, p+1, hi, )
	return a, sum(count)

for i in range(0, 100):
	a = []
	for j in range(0,10):
		a.append( random.randrange(1,100))
	print(quickSort(a, 0, len(a)-1 ))