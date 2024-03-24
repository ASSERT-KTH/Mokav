def func(*args):
	ret_values = []
	
	s = args[0]
	i = 0
	count = 0
	ans = False
	while (i < (len(s) - 1)):
	    if (s[i] == s[(i + 1)]):
	        count = (count + 1)
	        if (count == 6):
	            ans = True
	            break
	    else:
	        count = 0
	    i = (i + 1)
	if (ans == True):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
