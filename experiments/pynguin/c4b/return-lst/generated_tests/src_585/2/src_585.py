def func(*args):
	ret_values = []
	
	word = args[0]
	last = 3
	count = 1
	for i in word:
	    if (last == i):
	        count += 1
	        if (count > 6):
	            ret_values.append('YES')
	            quit()
	    else:
	        count = 1
	    last = i
	ret_values.append('NO')

	return ret_values
