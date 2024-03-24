def func(*args):
	ret_values = []
	
	s = args[0]
	if ((len(s) > 0) and (len(s) < 101)):
	    if (s.find('h') != (- 1)):
	        h1 = s.find('h')
	        if (s.find('e', h1) != (- 1)):
	            e1 = s.find('e', h1)
	            if (s.find('l', e1) != (- 1)):
	                l1 = s.find('l', e1)
	                if (s.find('l', (l1 + 1)) != (- 1)):
	                    l2 = s.find('l', l1)
	                    if (s.find('o', l2) != (- 1)):
	                        ret_values.append('YES')
	                    else:
	                        ret_values.append('NO')
	                else:
	                    ret_values.append('NO')
	            else:
	                ret_values.append('NO')
	        else:
	            ret_values.append('NO')
	    else:
	        ret_values.append('NO')

	return ret_values
