def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	s = str(n)
	(cnt4, cnt7) = (0, 0)
	for i in range(len(s)):
	    if (s[i] == '7'):
	        cnt7 += 1
	    if (s[i] == '4'):
	        cnt4 += 1
	if (((cnt4 + cnt7) == 7) or ((cnt4 + cnt7) == 4)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list