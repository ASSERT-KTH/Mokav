def func(*args):
	ret_values = []
	
	chair_pst = {'f': 1, 'e': 2, 'd': 3, 'a': 4, 'b': 5, 'c': 6}
	(*row, chair) = args[0]
	row = int(''.join(row))
	seconds = ((((row - 1) // 4) * 2) * 6)
	left = (row % 4)
	if ((left == 2) or (left == 0)):
	    seconds += 6
	seconds += chair_pst[chair]
	if ((left == 0) or (left == 3)):
	    seconds += (row - 3)
	else:
	    seconds += (row - 1)
	ret_values.append(seconds)

	return ret_values
