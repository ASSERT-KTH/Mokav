def func(*args):
	ret_values = []
	
	s = args[0]
	f = s[:(len(s) // 2)]
	if ((len(s) % 2) != 0):
	    b = s[((len(s) // 2) + 1):]
	else:
	    b = s[(len(s) // 2):]
	b = b[::(- 1)]
	flag = 0
	for i in range(len(f)):
	    if (f[i] != b[i]):
	        flag += 1
	if ((flag == 1) or ((flag == 0) and ((len(s) % 2) != 0))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
