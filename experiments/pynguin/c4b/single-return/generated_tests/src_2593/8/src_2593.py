def func(*args):
	
	
	def rec(num):
	    mod = 10
	    if (num < mod):
	        return 0
	    pom = mod
	    i = 1
	    while (pom < (num // mod)):
	        i += 1
	        pom *= mod
	    res = (num % pom)
	    if ((num != 109) and ((((mod * num) // pom) % mod) == 9)):
	        return rec(res)
	    return res
	num = int(args[0])
	return((num - rec((num + 1))))
