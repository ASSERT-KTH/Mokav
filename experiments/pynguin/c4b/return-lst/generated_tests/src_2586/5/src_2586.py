def func(*args):
	ret_values = []
	
	
	def compute_sets(a, b, k):
	    if (not ((a >= k) or (b >= k))):
	        return (- 1)
	    awins = (a // k)
	    bwins = (b // k)
	    if (awins == 0):
	        if ((b % k) != 0):
	            return (- 1)
	    elif (bwins == 0):
	        if ((a % k) != 0):
	            return (- 1)
	    return (awins + bwins)
	
	def main():
	    import sys
	    for line in sys.stdin:
	        line = [int(x) for x in line.rstrip().split(' ')]
	        k = line[0]
	        a = line[1]
	        b = line[2]
	        ret_values.append(compute_sets(a, b, k))
	if (__name__ == '__main__'):
	    main()

	return ret_values
