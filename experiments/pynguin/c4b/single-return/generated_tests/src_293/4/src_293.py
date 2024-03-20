def func(*args):
	
	if (__name__ == '__main__'):
	    n = int(args[0])
	    prime = ([True] * 1000001)
	    for i in range(2, 1000000):
	        if prime[i]:
	            for j in range((i * i), 1000000, i):
	                prime[j] = False
	            if ((n % i) == 0):
	                while ((n % i) == 0):
	                    n //= i
	                n *= i
	    return(n)
