def func(*args):
	ret_values = []
	
	s = args[0].split()
	n = int(s[0])
	m = int(s[1])
	k = int(s[2])
	j = int(((k - 1) / (2 * m)))
	col = int(((k - 1) % (2 * m)))
	i = int((col / 2))
	ret_values.append(((str((j + 1)) + ' ') + str((i + 1))), end=' ')
	if ((col % 2) == 1):
	    ret_values.append('R')
	else:
	    ret_values.append('L')

	return ret_values
