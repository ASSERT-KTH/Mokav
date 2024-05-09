def patched_func(*args):
	global_list = []
	
	import math, sys
	(a, b, n) = map(float, args[0].split())
	if ((a == 0) and (b == 0)):
	    global_list.append(5)
	    sys.exit()
	try:
	    ans = math.pow(abs((b / a)), (1 / n))
	    if (((n % 2) == 1) and ((b / a) < 0)):
	        ans *= (- 1)
	except:
	    global_list.append('No solution')
	    sys.exit()
	if (math.ceil(abs(ans)) == math.floor((abs(ans) + 5e-11))):
	    global_list.append((int((abs(ans) + 5e-11)) * ((- 1) if (ans < 0) else 1)))
	else:
	    global_list.append('No solution')
	return global_list