def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = args[1]
	if ((s.count('7') + s.count('4')) != len(s)):
	    ret_values.append('NO')
	else:
	    s1 = 0
	    s2 = 0
	    for i in s[:(n // 2)]:
	        s1 += int(i)
	    for i in s[(n // 2):]:
	        s2 += int(i)
	    if (s1 == s2):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
