def func(*args):
	ret_values = []
	
	input_str = args[0]
	count = 0
	for c in range(0, len(input_str)):
	    if (c == (len(input_str) - 1)):
	        if (count >= 6):
	            ret_values.append('YES')
	            break
	        else:
	            count = 0
	            break
	    if (input_str[c] == input_str[(c + 1)]):
	        count += 1
	    else:
	        if (count >= 6):
	            ret_values.append('YES')
	            break
	        count = 0
	if (count == 0):
	    ret_values.append('NO')

	return ret_values
