def func(*args):
	ret_values = []
	
	
	def get_ints(string):
	    return list(map(int, string.split()))
	
	def get_input():
	    a = get_ints(args[0])
	    return a
	
	def sieve(x):
	    res = []
	    xs = list(range(2, (x + 1)))
	    i = 0
	    while (i < len(xs)):
	        e = xs[i]
	        j = 0
	        while (j < len(xs)):
	            if (((xs[j] % e) == 0) and (xs[j] != e)):
	                del xs[j]
	                j -= 1
	            j += 1
	        res.append(e)
	        i += 1
	    return res
	
	def main():
	    (n, m) = get_input()
	    p = sieve(m)
	    res = ('NO' if ((m not in p) or ((p.index(m) - p.index(n)) != 1)) else 'YES')
	    ret_values.append(res)
	    return res
	if (__name__ == '__main__'):
	    main()

	return ret_values
