def patched_func(*args):
	global_list = []
	
	s = args[0]
	l = list(s.lower())
	k = list(s.lower())
	v = ['a', 'o', 'y', 'e', 'u', 'i']
	count = 0
	for i in range(len(l)):
	    if (l[i] in v):
	        k.remove(l[i])
	        count = (count - 1)
	    else:
	        k.insert((i + count), '.')
	        count = (count + 1)
	s2 = ''.join(k)
	global_list.append(s2)
	return global_list