def func(*args):
	ret_values = []
	
	s = args[0]
	h = int(s[:2])
	m = int(s[3:])
	mm = int((s[1] + s[0]))
	if ((h == 6) or (h == 7)):
	    ret_values.append((('10' + ':') + '01'))
	elif ((h == 8) or (h == 9)):
	    ret_values.append((('10' + ':') + '01'))
	elif ((h == 16) or (h == 17)):
	    ret_values.append('20:02')
	elif ((h == 18) or (h == 19)):
	    ret_values.append('20:02')
	elif ((h == 5) and (m > 49)):
	    ret_values.append('10:01')
	elif ((h == 15) and (m > 50)):
	    ret_values.append('20:02')
	elif (m < mm):
	    ret_values.append((((s[0] + s[1]) + ':') + str(mm)))
	else:
	    h = ((h + 1) % 24)
	    if (h < 10):
	        h = ('0' + str(h))
	        ret_values.append((((h + ':') + h[1]) + h[0]))
	    else:
	        t = str(h)
	        ret_values.append((((t + ':') + t[1]) + t[0]))

	return ret_values
