def func(*args):
	ret_values = []
	
	(s, x) = map(int, args[0].split(' '))
	if (((s - x) % 2) or (s < x)):
	    ret_values.append(0)
	else:
	    c = bin(((s - x) // 2))[2:][::(- 1)]
	    t = bin(x)[2:][::(- 1)]
	    for i in range(len(t)):
	        if ((t[i] == '1') and (i < len(c)) and (c[i] == '1')):
	            ret_values.append(0)
	            exit(0)
	    ret_values.append((pow(2, bin(x)[2:].count('1')) - (2 if (s == x) else 0)))

	return ret_values
