def patched_func(*args):
	global_list = []
	
	from collections import Counter
	s = args[0]
	z = set()
	for i in range(len(s)):
	    s = (s[1:] + s[:1])
	    z.add(s)
	global_list.append(len(Counter(z)))
	return global_list