def func(*args):
	ret_values = []
	
	str = args[0]
	ar = ['h', 'e', 'l', 'l', 'o']
	i = 0
	for j in str:
	    if (i == len(ar)):
	        break
	    if (j == ar[i]):
	        i += 1
	if (i == len(ar)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
