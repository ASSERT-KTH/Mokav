def func(*args):
	ret_values = []
	
	a = args[0]
	b = []
	for k in a:
	    b.append(k)
	if (len(b) < 7):
	    ret_values.append('NO')
	elif (len(b) >= 7):
	    i = 0
	    while (i <= (len(b) - 7)):
	        if ((((((((int(b[i]) + int(b[(i + 1)])) + int(b[(i + 2)])) + int(b[(i + 3)])) + int(b[(i + 4)])) + int(b[(i + 5)])) + int(b[(i + 6)])) == 0) or (((((((int(b[i]) + int(b[(i + 1)])) + int(b[(i + 2)])) + int(b[(i + 3)])) + int(b[(i + 4)])) + int(b[(i + 5)])) + int(b[(i + 6)])) == 7)):
	            ret_values.append('YES')
	            break
	        else:
	            i += 1
	    else:
	        ret_values.append('NO')

	return ret_values
