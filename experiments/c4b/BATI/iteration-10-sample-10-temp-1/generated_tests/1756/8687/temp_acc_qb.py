def patched_func(*args):
	global_list = []
	
	s = list(map(int, args[0].split()))
	se = set()
	for i in range(len(s)):
	    se.add(s[i])
	global_list.append((4 - len(se)))
	return global_list