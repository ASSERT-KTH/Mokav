def patched_func(*args):
	global_list = []
	
	s = args[0]
	n = len(s)
	z = ''
	k = 0
	mm = 0
	vk = 'VK'
	vv = 'VV'
	kk = 'KK'
	while (vk in s):
	    m = s.index(vk)
	    z = s[:m]
	    s = s[(m + 2):]
	    k += 1
	    if ((vv in z) or (kk in z)):
	        mm = 1
	if (k == 0):
	    z = s
	if ((vv in z) or (kk in z) or (vv in s) or (kk in s)):
	    mm = 1
	global_list.append((k + mm))
	return global_list