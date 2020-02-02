def queen(queens):
	if queens==[]:
		queens.append(0)
	for i in range(8):
		for j in range(8):
			print(queens)
			if queens[i]-i!=j-i+1 and queens[i]+i!=j+i+1 and queens[i]!=j :
				print(queens[i]-i==j-i+1 ,j)
				for k in range(len(queens)):
					if queens[k] == j:
						break
					if k == len(queens)-1:	
						queens.append(j)
	if len(queens)<8:
		return 0
	return queens
		
	
				
	
queens = []
print(queen(queens))
	
		