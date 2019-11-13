numbers = []
def getNumbers( text ):
	
	"""
	Parameters
	----------
	text : str
		text has the text that need to be filtered.
	tmp : str
		tmp has an empty string, this is were we put in the numbers.
	numbers : list
		numbers is were we put in the numbers that we found.
		
	Returns
	-------
	numbers : list
		Returns the numbers in the text
	"""
	
	tmp=""
	for i in range( 0, len( text ) ):
		if text[i].isdigit():
			tmp +=  str(text[i]) 
			if  text[i+1].isdigit() != 1 :
				numbers.append( int(tmp)  )
				tmp=""
	return numbers
	
text = 'een123zin45 6met-632meerdere+7777getallen'
print( getNumbers( text ) )