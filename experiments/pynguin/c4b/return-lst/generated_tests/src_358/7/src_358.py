def func(*args):
	ret_values = []
	
	n = args[0]
	hi = n.find('h')
	ei = (- 1)
	li = (- 1)
	lli = (- 1)
	oi = (- 1)
	if (hi != (- 1)):
	    ei = n.find('e', (hi + 1))
	if (ei != (- 1)):
	    li = n.find('l', (ei + 1))
	if (li != (- 1)):
	    lli = n.find('l', (li + 1))
	if (lli != (- 1)):
	    oi = n.find('o', (lli + 1))
	if ((hi != (- 1)) and (ei != (- 1)) and (li != (- 1)) and (lli != (- 1)) and (oi != (- 1))):
	    if (hi < ei < li < lli < oi):
	        ret_values.append('YES')
	        exit(0)
	ret_values.append('NO')

	return ret_values
