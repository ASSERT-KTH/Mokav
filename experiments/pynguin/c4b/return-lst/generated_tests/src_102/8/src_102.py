def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
	b = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]
	s = hex(n)
	l = 0
	for i in range(2, len(s)):
	    l += b[a.index(s[i])]
	ret_values.append(l)

	return ret_values
