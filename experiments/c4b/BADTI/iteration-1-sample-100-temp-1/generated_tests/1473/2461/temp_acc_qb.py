def patched_func(*args):
	global_list = []
	
	
	def rt(p):
	    a = (((p[0] - p[2]) ** 2) + ((p[1] - p[3]) ** 2))
	    b = (((p[0] - p[4]) ** 2) + ((p[1] - p[5]) ** 2))
	    c = (((p[2] - p[4]) ** 2) + ((p[3] - p[5]) ** 2))
	    return (a and b and c and (((a + b) == c) or ((a + c) == b) or ((b + c) == a)))
	
	def f(p):
	    if rt(p):
	        return 'RIGHT'
	    for i in range(6):
	        p[i] -= 1
	        if rt(p):
	            return 'ALMOST'
	        p[i] += 2
	        if rt(p):
	            return 'ALMOST'
	        p[i] -= 1
	    return 'NEITHER'
	global_list.append(f(list(map(int, args[0].split()))))
	return global_list