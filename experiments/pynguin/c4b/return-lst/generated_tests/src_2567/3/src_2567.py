def func(*args):
	ret_values = []
	
	s = args[0]
	s = s.split(' ')
	l = [int(s[0]), int(s[1]), int(s[2]), int(s[3])]
	l.sort()
	tmp = l[0]
	if ((l[0] + l[1]) > l[2]):
	    ret_values.append('TRIANGLE')
	else:
	    l.pop(0)
	    if ((l[0] + l[1]) > l[2]):
	        ret_values.append('TRIANGLE')
	    else:
	        l.append(tmp)
	        l.sort()
	        if (((l[0] + l[1]) == l[2]) or ((l[1] + l[2]) == l[3])):
	            ret_values.append('SEGMENT')
	        else:
	            ret_values.append('IMPOSSIBLE')

	return ret_values
