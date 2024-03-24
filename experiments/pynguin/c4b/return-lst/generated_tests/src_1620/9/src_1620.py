def func(*args):
	ret_values = []
	
	V = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
	C = ['b', 'B', 'c', 'C', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'v', 'V', 'w', 'W', 'x', 'X', 'z', 'Z']
	s = [x for x in args[0] if x.isalpha()]
	if (s[(- 1)] in V):
	    ret_values.append('YES')
	elif (s[(- 1)] in C):
	    ret_values.append('NO')

	return ret_values
