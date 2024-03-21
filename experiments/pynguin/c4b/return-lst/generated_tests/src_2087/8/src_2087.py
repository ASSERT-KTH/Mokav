def func(*args):
	ret_values = []
	
	line = args[0]
	result = 0
	maxi = 1
	for x in range(1, len(line)):
	    if (line[x] == line[(x - 1)]):
	        maxi += 1
	        if (maxi > result):
	            result = maxi
	    else:
	        if (maxi > result):
	            result = maxi
	        maxi = 1
	if (result >= 7):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
