def func(*args):
	ret_values = []
	
	s = args[0]
	ans = ''
	l = ['a', 'e', 'i', 'o', 'u', 'y', 'Y', 'A', 'E', 'I', 'O', 'U']
	for i in s:
	    if (i not in l):
	        ans = ((ans + '.') + i.lower())
	ret_values.append(ans)

	return ret_values
