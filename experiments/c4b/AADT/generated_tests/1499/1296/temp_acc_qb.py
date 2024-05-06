def patched_func(*args):
	global_list = []
	
	MOD = 1000000007
	n = int(args[0])
	if (n == 0):
	    global_list.append(1)
	else:
	    global_list.append((((2 * pow(4, (n - 1), MOD)) + pow(2, (n - 1), MOD)) % MOD))
	return global_list