def original_func(*args):
	global_list = []
	
	n = int(args[0])
	j = 0
	s = str(n)
	k = len(s)
	l = int((n / 4))
	m = int((n / 7))
	for i in range(k):
	    if (s[i] == 0):
	        break
	    elif (((int(s[i]) / 4) == 1) or ((int(s[i]) / 7) == 1)):
	        j = (j + 1)
	    elif ((n == (l * l)) or (n == (m * m))):
	        j = (j + 1)
	if (j == 0):
	    global_list.append('NO')
	elif (j == k):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list