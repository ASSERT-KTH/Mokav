def func(*args):
	ret_values = []
	
	s = str(args[0])
	a = ['h', 'e', 'l', 'l', 'o']
	j = 0
	for k in range(len(a)):
	    if (a[k] in s):
	        j += 1
	        y = s.index(a[k])
	        s = s[(y + 1):]
	if (j == 5):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
