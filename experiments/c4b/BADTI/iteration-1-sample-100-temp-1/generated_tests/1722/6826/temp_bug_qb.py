def original_func(*args):
	global_list = []
	
	import math
	
	def check(s1, s2):
	    for i in range(len(s1)):
	        for j in range(len(s2)):
	            if (s1[i] == s2[j]):
	                return True
	    return False
	N = int(args[0])
	div = 0
	bound = math.ceil(math.sqrt(N))
	for i in range(bound):
	    k = (i + 1)
	    if ((N % k) == 0):
	        f1 = str(k)
	        f2 = str((N // k))
	        if check(f1, str(N)):
	            div += 1
	        if ((f1 != f2) and check(f2, str(N))):
	            div += 1
	global_list.append(div)
	return global_list