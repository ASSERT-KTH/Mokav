def func(*args):
	ret_values = []
	
	s = args[0]
	S = s.split()
	h1 = int(S[0])
	h2 = int(S[1])
	s = args[1]
	S = s.split()
	a = int(S[0])
	b = int(S[1])
	time = 14
	if (((h1 + (a * 8)) < h2) and ((a * 12) <= (b * 12))):
	    ret_values.append('-1')
	elif ((h1 + (a * 8)) >= h2):
	    ret_values.append('0')
	else:
	    h1 += (a * 8)
	    h1 -= (b * 12)
	    h1 += (a * 12)
	    if (h1 >= h2):
	        ret_values.append('1')
	    elif (((h2 - h1) / ((a * 12) - (b * 12))) > int(((h2 - h1) / ((a * 12) - (b * 12))))):
	        ret_values.append((int(((h2 - h1) / ((a * 12) - (b * 12)))) + 2))
	    else:
	        ret_values.append((int(((h2 - h1) / ((a * 12) - (b * 12)))) + 1))

	return ret_values
