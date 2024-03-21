def func(*args):
	ret_values = []
	
	string = args[0]
	t = 0
	if (len(string) < 7):
	    ret_values.append('NO')
	else:
	    for x in range((len(string) - 6)):
	        if ((string[x:(x + 7)] == '1111111') or (string[x:(x + 7)] == '0000000')):
	            t += 1
	            ret_values.append('YES')
	            break
	    if (t == 0):
	        ret_values.append('NO')

	return ret_values
