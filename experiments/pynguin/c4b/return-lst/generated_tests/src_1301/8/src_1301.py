def func(*args):
	ret_values = []
	
	(s, x) = args[0].split()
	(s, x) = (int(s), int(x))
	ones_in_x = 0
	for let in reversed('{0:b}'.format(x)):
	    if (let == '1'):
	        ones_in_x += 1
	zbytkove = (s - x)
	if (((zbytkove % 2) == 1) or (x > s)):
	    ret_values.append(0)
	elif (s == x):
	    ret_values.append(((2 ** ones_in_x) - 2))
	else:
	    for (zb, let) in zip(reversed('{0:b}'.format((zbytkove // 2))), reversed('{0:b}'.format(x))):
	        if ((zb == '1') and (zb == let)):
	            ret_values.append(0)
	            break
	    else:
	        ret_values.append((2 ** ones_in_x))

	return ret_values
