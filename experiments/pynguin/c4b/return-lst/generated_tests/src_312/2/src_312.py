def func(*args):
	ret_values = []
	
	MOD = 1000000007
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	else:
	    ret_values.append((((2 * pow(4, (n - 1), MOD)) + pow(2, (n - 1), MOD)) % MOD))

	return ret_values
