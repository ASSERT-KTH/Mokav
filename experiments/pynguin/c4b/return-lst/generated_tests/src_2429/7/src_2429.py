def func(*args):
	ret_values = []
	
	import fileinput
	
	def main():
	    line = fileinput.input().readline().split(' ')
	    n = int(line[0])
	    k = int(line[1])
	    hi = n
	    lo = 0
	    while (lo < hi):
	        mid = (lo + ((hi - lo) // 2))
	        if is_enough(mid, n, k):
	            hi = mid
	        else:
	            lo = (mid + 1)
	    ret_values.append(lo)
	
	def is_enough(v, target, k):
	    '\n    Increase the powers of k until k^p >= v or tally exceeds target.\n    '
	    k_pow = 1
	    tally = 0
	    for _ in range(v):
	        factor = (v // k_pow)
	        tally += factor
	        if (tally >= target):
	            return True
	        elif (factor == 0):
	            return False
	        k_pow *= k
	main()

	return ret_values
