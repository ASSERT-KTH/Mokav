def func(*args):
	ret_values = []
	
	s = args[0]
	index = s.find('h')
	if (index != (- 1)):
	    index = s.find('e', (index + 1))
	    if (index != (- 1)):
	        index = s.find('l', (index + 1))
	        if (index != (- 1)):
	            index = s.find('l', (index + 1))
	            if (index != (- 1)):
	                index = s.find('o', (index + 1))
	                if (index != (- 1)):
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
