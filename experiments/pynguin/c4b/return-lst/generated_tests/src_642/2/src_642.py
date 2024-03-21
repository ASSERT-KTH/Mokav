def func(*args):
	ret_values = []
	
	
	def main():
	    from itertools import combinations
	    (s, res) = (args[0], ())
	    for le in range(len(s)):
	        for p in combinations(s, (le + 1)):
	            if ((res < p) and (p == p[::(- 1)])):
	                res = p
	    ret_values.append(''.join(res))
	if (__name__ == '__main__'):
	    main()

	return ret_values
