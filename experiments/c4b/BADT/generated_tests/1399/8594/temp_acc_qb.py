def patched_func(*args):
	global_list = []
	
	import math
	
	def prost(x):
	    for i in range(2, (int(math.sqrt(x)) + 1)):
	        if ((x % i) == 0):
	            return False
	    return True
	(n, k) = [int(s) for s in args[0].split()]
	if (k == 0):
	    global_list.append('YES')
	else:
	    a = []
	    for i in range(2, (n + 1)):
	        if prost(i):
	            a.append(i)
	    cnt = 0
	    for i in range(2, len(a)):
	        b = [((a[(j - 1)] + a[j]) + 1) for j in range(2, i)]
	        if (a[i] in b):
	            cnt += 1
	            if (cnt >= k):
	                global_list.append('YES')
	                break
	    else:
	        global_list.append('NO')
	return global_list