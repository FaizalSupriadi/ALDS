def money( a, i ,j ):

	"""
	Parameters
	----------
	matrix : list
		matrix has a list with values we need to check
	
	a : list
		a is the given list
	
	i : int
		i is a value needed to itterate trough the list
	j : int 
		j is a value needed to itterate trough list[i]
		
	Returns
	-------
	money(a,i,j) : function
		return to itself to create a recursive function
	a : list
		return a list with the amount of ways you can combine the money
	"""
	m = [ 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000 ]
	
	
	
	if a[i][0]==a[i][j]:
		a[i][0]=1

	if a[0][j]==a[i][j]:
		a[0][j] = 1

	elif j >= m[i]:
		a[i][j] = a[i-1][j] + a[i][j-m[i]]

	elif j < m[i]:
		a[ i][j] = a[i-1][j]
	
	j+=1
	if j == len(a[i]):
		i+=1
		if i == len(a):
			return a
		j = 0
	
	return money(a, i, j )


matrix = [[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]]

print(money(matrix, 0, 0 ))
