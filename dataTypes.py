def data_type(argumnt): 
  #check for string datatype
	if isinstance(argumnt, str):
		return len(argumnt)
		
	#check for None datatype
	if argumnt is None:
		return 'no value'
		
	#check for bool datatyoe
	if isinstance(argumnt, bool):
		return argumnt
		
	#check for int datatype
	if isinstance(argumnt, int):
		if argumnt < 100:
			return 'less than 100'
		elif argumnt > 100:
			return 'more than 100'
		else:
			return 'equal to 100'
			
  #check for list datatype
	if isinstance(argumnt, list):
		if len(argumnt) >= 3:
			return argumnt[2]
		else:
			return None

print data_type(12)
			
			