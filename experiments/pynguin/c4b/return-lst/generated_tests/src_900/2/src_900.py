def func(*args):
	ret_values = []
	
	s = args[0]
	i = 0
	j = 0
	x = 'hello'
	while (i < len(s)):
	    if (s[i] == x[j]):
	        j += 1
	    i += 1
	    if (j == 5):
	        ret_values.append('YES')
	        break
	    if (i == len(s)):
	        ret_values.append('NO')
	        break

	return ret_values
