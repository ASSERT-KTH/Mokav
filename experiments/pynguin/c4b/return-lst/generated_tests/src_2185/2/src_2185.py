def func(*args):
	ret_values = []
	
	import math, sys
	(a, b, n) = map(float, args[0].split())
	if ((a == 0) and (b == 0)):
	    ret_values.append(5)
	    sys.exit()
	try:
	    ans = math.pow(abs((b / a)), (1 / n))
	    if (((n % 2) == 1) and ((b / a) < 0)):
	        ans *= (- 1)
	except:
	    ret_values.append('No solution')
	    sys.exit()
	if (math.ceil(abs(ans)) == math.floor((abs(ans) + 5e-11))):
	    ret_values.append((int((abs(ans) + 5e-11)) * ((- 1) if (ans < 0) else 1)))
	else:
	    ret_values.append('No solution')

	return ret_values
