def prime1000():
	array =[]
	for i in range(0, 1000):
		if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i!=1 or i==2 or i==3 or i==5 or i==7:
			array.append(i)
	return array

print(prime1000())