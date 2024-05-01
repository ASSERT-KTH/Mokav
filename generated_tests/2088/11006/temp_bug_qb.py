def original_func(*args):
	global_list = []
	
	s1 = args[0]
	s2 = args[1]
	s3 = args[2]
	s4 = args[3]
	i = 0
	f = False
	while ((i < 3) and (f == False)):
	    if (((s1[i] == s2[i]) and (s1[(i + 1)] == s2[(i + 1)])) or ((s1[i] == s2[i]) and (s1[(i + 1)] != s2[(i + 1)])) or ((s1[i] != s2[i]) and (s1[(i + 1)] == s2[(i + 1)]))):
	        f = True
	    i += 1
	i = 0
	while ((i < 3) and (f == False)):
	    if (((s2[i] == s3[i]) and (s2[(i + 1)] == s3[(i + 1)])) or ((s2[i] == s3[i]) and (s2[(i + 1)] != s3[(i + 1)])) or ((s2[i] != s3[i]) and (s2[(i + 1)] == s3[(i + 1)]))):
	        f = True
	    i += 1
	i = 0
	while ((i < 3) and (f == False)):
	    if (((s3[i] == s4[i]) and (s3[(i + 1)] == s4[(i + 1)])) or ((s3[i] == s4[i]) and (s3[(i + 1)] != s4[(i + 1)])) or ((s3[i] != s4[i]) and (s3[(i + 1)] == s4[(i + 1)]))):
	        f = True
	    i += 1
	if f:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list