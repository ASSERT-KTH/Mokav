def original_func(*args):
	global_list = []
	
	(b, d, s) = map(int, args[0].split(' '))
	if ((b == d) and (d == s)):
	    global_list.append('0')
	elif ((b != d) and (d != s) and (b != s)):
	    count1 = 0
	    k = (max(b, d, s) - 1)
	    if ((k - b) > 0):
	        count1 += (b - k)
	    if ((k - d) > 0):
	        count1 += (k - d)
	    if ((k - s) > 0):
	        count1 += (k - s)
	    global_list.append(count1)
	elif ((b == 0) and (d == 0) and (s != 0)):
	    global_list.append(((s - 1) * 2))
	elif ((b != 0) and (d == 0) and (s == 0)):
	    global_list.append(((b - 1) * 2))
	elif ((d != 0) and (b == 0) and (s == 0)):
	    global_list.append(((d - 1) * 2))
	elif ((b == d) and (d != s)):
	    if (b > s):
	        global_list.append(((b - 1) - s))
	    else:
	        global_list.append((((s - 1) - b) * 2))
	elif ((b == s) and (s != d)):
	    if (b > d):
	        global_list.append(((b - 1) - d))
	    else:
	        global_list.append((((d - 1) - b) * 2))
	elif ((s == d) and (s != b)):
	    if (s > b):
	        global_list.append(((d - 1) - b))
	    else:
	        global_list.append((((b - 1) - d) * 2))
	return global_list