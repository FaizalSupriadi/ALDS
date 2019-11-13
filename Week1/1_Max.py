currentMax = 0
def max( array ):
	"""
	Parameters
	----------
	array : list
		The array has the values that need to be checked.

	Returns
	-------
	currentMax : int
		currentMax has the value that is currently the biggest number.
	"""
	currentMax = array[0]
	for i in range( 0, len( array  ) ):
		if array[i] > currentMax:
			currentMax = array[i]
	return currentMax

array = [5, 6, 1, 8, 2, 123, 14 ]
print( max(array) )