def avgHairLength( hair ):
	avgHair=0
	for i in range( 0, len(hair) ):
		if hair[i] != str:
			avgHair+=hair[i]
	if avgHair != 0:
		avgHair = avgHair / len(hair)
	return avgHair

def group( students ):
	result = [(),(),()]
	m=0		
	for i in range(0, len(students) ):
		for j in range(i+1, len(students) ):
			for k in range(j+1, len(students) ):

				tup = (students[i], students[j], students[k] )
				relativeHair = avgHairLength( tup ) - avgHairLength( list( set(students) - set(tup) ) )
				print(tup, list( set(students) - set(tup)))
				result[m] = (tup, relativeHair)
				m+=1
				if m>2:
					m=0
	return result
students = [1, 2, 3,4 ,5 ,6]
test = group(students)
print(test)