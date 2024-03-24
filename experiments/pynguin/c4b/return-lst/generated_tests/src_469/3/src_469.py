def func(*args):
	ret_values = []
	
	n = str(args[0].strip())
	c = 0
	for i in n:
	    if ((i == '7') or (i == '4')):
	        fl = True
	        c += 1
	    else:
	        fl = False
	if ((c == 7) or (c == 4)):
	    ret_values.append('YES')
	elif ((fl == True) and ((c == 7) or (c == 4))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
