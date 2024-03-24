def func(*args):
	ret_values = []
	
	import sys
	
	def main():
	    ret_values.append(power(1378, int(sys.stdin.readline()), mod=10))
	
	def power(a, n, mod):
	    cur_power = a
	    ans = 1
	    for i in range(32):
	        if (n & (1 << i)):
	            ans *= cur_power
	        cur_power *= cur_power
	        cur_power %= mod
	    ans %= mod
	    return ans
	if (__name__ == '__main__'):
	    main()

	return ret_values
