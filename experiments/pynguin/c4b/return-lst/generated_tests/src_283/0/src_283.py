def func(*args):
	ret_values = []
	
	s = args[0]
	counter = 0
	hi = 'hello'
	for i in range(len(s)):
	    if (s[i] == hi[counter]):
	        counter += 1
	    if (counter == 5):
	        break
	if (counter == 5):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
