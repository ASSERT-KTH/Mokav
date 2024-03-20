def func(*args):
	
	
	def compute():
	    (A, B, n, x) = map(int, args[0].split())
	    MOD = int((1000000000.0 + 7))
	    i = ((pow(A, n, MOD) * x) % MOD)
	    if (A == 1):
	        j = (B * n)
	    else:
	        j = (((B * (pow(A, n, MOD) - 1)) * pow((A - 1), (MOD - 2), MOD)) % MOD)
	    return str(((i + j) % MOD))
	if (__name__ == '__main__'):
	    return(compute())
