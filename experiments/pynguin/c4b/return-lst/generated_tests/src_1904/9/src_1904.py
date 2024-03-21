def func(*args):
	ret_values = []
	
	lukcyNumbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
	givenNumber = int(args[0])
	for number in lukcyNumbers:
	    if ((givenNumber % number) == 0):
	        ret_values.append('YES')
	        exit()
	ret_values.append('NO')

	return ret_values
