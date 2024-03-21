def func(*args):
	ret_values = []
	
	s = args[0]
	len_s = len(s)
	t = 'hello'
	j = 0
	count = 0
	for i in t:
	    while True:
	        if (j == len_s):
	            break
	        elif (i == s[j]):
	            count += 1
	            j += 1
	            break
	        elif (i != s[j]):
	            j += 1
	if (count == 5):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
