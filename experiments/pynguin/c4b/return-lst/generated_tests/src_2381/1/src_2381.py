def func(*args):
	ret_values = []
	
	arr = args[0]
	it1 = 0
	it2 = 0
	for i in arr:
	    if (i == '1'):
	        it1 += 1
	        it2 = 0
	    else:
	        it2 += 1
	        it1 = 0
	    if ((it1 == 7) or (it2 == 7)):
	        break
	if ((it1 == 7) or (it2 == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
