def func(*args):
	ret_values = []
	
	s = str(args[0])
	i = 0
	zero = 0
	zeroS = 0
	one = 0
	oneS = 0
	while (i < len(s)):
	    if (s[i] == '0'):
	        one = 0
	        zero += 1
	        if (zeroS < zero):
	            zeroS = zero
	    else:
	        zero = 0
	        one += 1
	        if (oneS < one):
	            oneS = one
	    i += 1
	if ((oneS >= 7) or (zeroS >= 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
