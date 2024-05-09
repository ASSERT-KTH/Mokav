def patched_func(*args):
	global_list = []
	
	
	def gcd(a, b):
	    while b:
	        (a, b) = (b, (a % b))
	    return a
	(a, b, c) = map(int, args[0].split())
	g = gcd(a, b)
	if ((c % g) != 0):
	    global_list.append('No')
	else:
	    a //= g
	    b //= g
	    c //= g
	    for i in range(((c // a) + 1)):
	        done = False
	        for j in range(((c // b) + 1)):
	            v = ((a * i) + (b * j))
	            if (v == c):
	                global_list.append('Yes')
	                done = True
	                break
	            elif (v > c):
	                break
	        if done:
	            break
	    else:
	        global_list.append('No')
	return global_list