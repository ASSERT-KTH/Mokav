def func(*args):
	
	
	def almostPrime(n):
	    s = set()
	    for i in range(2, (int((n ** 0.5)) + 1)):
	        if ((n % i) == 0):
	            s.add(i)
	        if (len(s) > 2):
	            return False
	        while ((n % i) == 0):
	            n /= i
	    if (n > 1):
	        s.add(n)
	    return (len(s) == 2)
	n = int(args[0])
	cnt = 0
	for i in range(1, (n + 1)):
	    cnt += almostPrime(i)
	return(cnt)
