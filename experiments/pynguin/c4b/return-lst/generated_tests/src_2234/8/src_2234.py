def func(*args):
	ret_values = []
	
	text = args[0]
	ALF = 'HQ9'
	count = 0
	for ch in text:
	    if (ch in ALF):
	        ret_values.append('YES')
	        break
	    else:
	        count += 1
	if (count == len(text)):
	    ret_values.append('NO')

	return ret_values
