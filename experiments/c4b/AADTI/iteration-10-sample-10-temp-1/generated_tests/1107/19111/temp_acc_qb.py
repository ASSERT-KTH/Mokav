def patched_func(*args):
	global_list = []
	
	a = list(args[0].split())
	a[0] = int(a[0])
	a[1] = int(a[1])
	stos = int(a[2])
	
	def gcd(x, y):
	    while y:
	        (x, y) = (y, (x % y))
	    return x
	res = False
	while True:
	    t = gcd(a[res], stos)
	    if ((stos - t) < 0):
	        global_list.append(int((not res)))
	        break
	    else:
	        stos -= t
	    res = (not res)
	return global_list