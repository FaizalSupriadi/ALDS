def prime1000():
	"""
	Parameters
	----------
	array : list
		The array is an empty list where all prime numbers will be appended
	i : int
		i has the range we need to check

	Returns
	-------
	array : list
		An array with prime numbers
	"""
	array =[]
	for i in range(2, 1000):
		if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 or i==2 or i==3 or i==5 or i==7:
			array.append(i)
	return array

print(prime1000())