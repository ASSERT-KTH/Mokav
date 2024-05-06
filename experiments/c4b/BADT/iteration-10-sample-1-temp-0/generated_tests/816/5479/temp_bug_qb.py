def original_func(*args):
	global_list = []
	
	s = args[0]
	s = s.split()
	ans = 0
	for i in range(3):
	    s[i] = int(s[i])
	if ((s[0] != s[1]) and (s[1] != s[2]) and (s[0] != s[2])):
	    Max = s[0]
	    Max_id = 0
	    for i in range(1, 3):
	        if (s[i] > Max):
	            Max = s[i]
	            Max_id = i
	    if (Max_id == 0):
	        ans = ((((2 * Max) - 2) - s[1]) - s[2])
	    elif (Max_id == 1):
	        ans = ((((2 * Max) - 1) - s[0]) - s[2])
	    elif (Max_id == 2):
	        ans = ((((2 * Max) - 2) - s[0]) - s[1])
	elif ((s[0] == s[1]) and (s[0] != s[2])):
	    if (s[0] > s[2]):
	        ans = ((s[0] - 1) - s[2])
	    else:
	        ans = (2 * ((s[2] - 1) - s[0]))
	elif ((s[0] == s[2]) and (s[0] != s[1])):
	    if (s[1] < s[0]):
	        ans = ((s[0] - 1) - s[1])
	    else:
	        ans = ((((2 * s[1]) - 1) - s[0]) - s[2])
	elif ((s[1] == s[2]) and (s[0] != s[2])):
	    if (s[1] > s[0]):
	        ans = ((s[1] - 1) - s[0])
	    else:
	        ans = (2 * ((s[0] - 1) - s[1]))
	else:
	    ans = 0
	global_list.append(ans)
	return global_list