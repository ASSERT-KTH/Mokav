def func(*args):
	ret_values = []
	
	n = list(args[0])
	count = 0
	for itch in n:
	    if ((itch == '4') or (itch == '7')):
	        count += 1
	if ((count == 4) or (count == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
