def patched_func(*args):
	global_list = []
	
	s = args[0]
	h = int(s[:2])
	m = int(s[3:])
	mm = int((s[1] + s[0]))
	if ((h == 6) or (h == 7)):
	    global_list.append((('10' + ':') + '01'))
	elif ((h == 8) or (h == 9)):
	    global_list.append((('10' + ':') + '01'))
	elif ((h == 16) or (h == 17)):
	    global_list.append('20:02')
	elif ((h == 18) or (h == 19)):
	    global_list.append('20:02')
	elif ((h == 5) and (m > 49)):
	    global_list.append('10:01')
	elif ((h == 15) and (m > 50)):
	    global_list.append('20:02')
	elif (m < mm):
	    global_list.append((((s[0] + s[1]) + ':') + str(mm)))
	else:
	    h = ((h + 1) % 24)
	    if (h < 10):
	        h = ('0' + str(h))
	        global_list.append((((h + ':') + h[1]) + h[0]))
	    else:
	        t = str(h)
	        global_list.append((((t + ':') + t[1]) + t[0]))
	return global_list