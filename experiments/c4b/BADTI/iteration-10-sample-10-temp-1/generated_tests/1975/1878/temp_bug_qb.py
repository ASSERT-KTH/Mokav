def original_func(*args):
	global_list = []
	
	import math
	inp = args[0].split()
	n = eval(inp[0])
	t = eval(inp[1])
	s = list(args[1])
	
	def swap(s):
	    for i in range((n - 2), (- 1), (- 1)):
	        if ((s[i] == 'B') and (s[(i + 1)] == 'G')):
	            s[i] = 'G'
	            s[(i + 1)] = 'B'
	    return s
	for i in range(t):
	    s = swap(s)
	global_list.append(''.join(s))
	return global_list