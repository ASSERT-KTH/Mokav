def func(*args):
	ret_values = []
	
	st = args[0]
	number = 0
	for c in st:
	    if ((c == '4') or (c == '7')):
	        number += 1
	if ((number == 4) or (number == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
