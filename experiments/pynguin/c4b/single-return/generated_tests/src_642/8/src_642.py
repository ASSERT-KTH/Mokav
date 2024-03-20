def func(*args):
	
	
	def main():
	    from itertools import combinations
	    (s, res) = (args[0], ())
	    for le in range(len(s)):
	        for p in combinations(s, (le + 1)):
	            if ((res < p) and (p == p[::(- 1)])):
	                res = p
	    return(''.join(res))
	if (__name__ == '__main__'):
	    main()
