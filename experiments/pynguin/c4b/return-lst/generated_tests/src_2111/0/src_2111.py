def func(*args):
	ret_values = []
	
	s = args[0]
	L = ['H', 'Q', '9']
	for i in range(len(s)):
	    if (s[i] in L):
	        ret_values.append('YES')
	        exit()
	ret_values.append('NO')

	return ret_values
