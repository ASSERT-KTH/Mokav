def original_func(*args):
	global_list = []
	
	
	def d():
	    (a, b, c) = map(int, args[0].split())
	    if ((c < b) and (c < a)):
	        return 'No'
	    if (((c % b) == 0) or ((c % a) == 0)):
	        return 'Yes'
	    q = max(a, b)
	    k = ((a + b) - q)
	    v = c
	    while (c > 0):
	        c -= q
	        if ((c % k) == 0):
	            return 'Yes'
	    c = v
	    while (c > 0):
	        c -= k
	        if ((c % q) == 0):
	            return 'Yes'
	    return 'No'
	global_list.append(d())
	return global_list