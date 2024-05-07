def original_func(*args):
	global_list = []
	
	s1 = list(map(int, args[0].split()))
	s2 = list(map(int, args[1].split()))
	s3 = list(map(int, args[2].split()))
	s4 = list(map(int, args[3].split()))
	if (((s1[0] == 1) and (s1[3] == 1)) or ((s1[1] == 1) and (s1[3] == 1)) or ((s1[2] == 1) and (s1[3] == 1)) or ((s2[0] == 1) and (s1[3] == 1)) or ((s3[1] == 1) and (s1[3] == 1)) or ((s4[2] == 1) and (s1[3] == 1)) or ((s2[0] == 1) and (s2[3] == 1)) or ((s2[1] == 1) and (s2[3] == 1)) or ((s2[1] == 1) and (s2[3] == 1)) or ((s3[0] == 1) and (s2[3] == 1)) or ((s4[1] == 1) and (s2[3] == 1)) or ((s1[2] == 1) and (s2[3] == 1)) or ((s3[0] == 1) and (s3[3] == 1)) or ((s3[1] == 1) and (s3[3] == 1)) or ((s3[1] == 1) and (s3[3] == 1)) or ((s4[0] == 1) and (s3[3] == 1)) or ((s1[1] == 1) and (s3[3] == 1)) or ((s2[2] == 1) and (s3[3] == 1)) or ((s4[0] == 1) and (s4[3] == 1)) or ((s4[1] == 1) and (s4[3] == 1)) or ((s4[1] == 1) and (s4[3] == 1)) or ((s1[0] == 1) and (s4[3] == 1)) or ((s2[1] == 1) and (s4[3] == 1)) or ((s3[2] == 1) and (s4[3] == 1))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list