def func(*args):
	ret_values = []
	
	A = args[0]
	c = 0
	count = 0
	for i in A:
	    if ((i == '4') or (i == '7')):
	        count = (count + 1)
	b = str(count)
	for i in b:
	    if ((i != '4') and (i != '7')):
	        c = 1
	        break
	if (c == 0):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
