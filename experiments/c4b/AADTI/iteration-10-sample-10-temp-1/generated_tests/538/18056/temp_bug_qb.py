def original_func(*args):
	global_list = []
	
	
	def cnt(s, v):
	    ans = 0
	    for i in s:
	        if (i == v):
	            ans += 1
	    return ans
	s = [int(z) for z in args[0].split()]
	mx = 0
	for i in range(1000):
	    mx = max(mx, (max(cnt(s, i), 3) * i))
	global_list.append((sum(s) - mx))
	return global_list