def find(lst, x):
	if lst == []:
		return-1
	if lst[0] == x :
		return 1
	lst = lst[1:]
	
	return find( lst, x )
	
	
lijst = [1, 2, 3, 4]
print(find( lijst, 10))