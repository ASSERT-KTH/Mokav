def original_func(*args):
	global_list = []
	
	MOD = 1000000007
	
	def power(b, p):
	    if (p == 0):
	        return 1
	    x = power(b, (p // 2))
	    x *= x
	    x %= MOD
	    if ((p % 2) == 1):
	        x *= b
	        x %= MOD
	    return x
	n = int(args[0])
	global_list.append(((int((((power(4, n) + power(2, n)) % MOD) // 2)) % MOD) % MOD))
	return global_list