def func(*args):
	ret_values = []
	
	import sys
	import math
	TESTING = False
	
	def solve():
	    (n,) = read()
	    if (n == 0):
	        return 1
	    MOD = 1000000007
	    return ((pow(2, (n - 1), MOD) + pow(2, ((2 * n) - 1), MOD)) % MOD)
	
	def read(mode=2):
	    inputs = args[0].strip()
	    if (mode == 0):
	        return inputs
	    if (mode == 1):
	        return inputs.split()
	    if (mode == 2):
	        return list(map(int, inputs.split()))
	
	def write(s='\n'):
	    if (s is None):
	        s = ''
	    if isinstance(s, list):
	        s = ' '.join(map(str, s))
	    s = str(s)
	    ret_values.append(s, end='')
	
	def run():
	    if TESTING:
	        sys.stdin = open('test.txt')
	    res = solve()
	    write(res)
	run()

	return ret_values
