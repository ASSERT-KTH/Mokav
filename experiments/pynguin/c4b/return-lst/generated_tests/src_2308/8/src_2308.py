def func(*args):
	ret_values = []
	
	s = args[0]
	cmp = ['h', 'e', 'l', 'l', 'o']
	for i in s:
	    if (i == cmp[0]):
	        cmp.pop(0)
	    if (cmp == []):
	        break
	ret_values.append(['NO', 'YES'][(cmp == [])])

	return ret_values
