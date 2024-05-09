def original_func(*args):
	global_list = []
	
	(s1, s2, s3) = map(int, args[0].split())
	for i in range(s1, 0, (- 1)):
	    if (((s1 % i) == 0) and ((s2 % i) == 0) and ((s3 % int((s2 / i))) == 0)):
	        global_list.append((((int((s1 / i)) * 4) + (i * 4)) + (int((s2 / i)) * 4)))
	        break
	return global_list