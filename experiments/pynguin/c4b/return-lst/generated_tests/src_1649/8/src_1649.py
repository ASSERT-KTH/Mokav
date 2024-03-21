def func(*args):
	ret_values = []
	
	word = args[0]
	goalCount = 0
	prev = word[0]
	for w in word:
	    if (w == prev):
	        goalCount += 1
	    else:
	        goalCount = 0
	    if (goalCount == 6):
	        ret_values.append('YES')
	        exit()
	    prev = w
	ret_values.append('NO')

	return ret_values
