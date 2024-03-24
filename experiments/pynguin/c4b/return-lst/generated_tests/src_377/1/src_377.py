def func(*args):
	ret_values = []
	
	import math
	n = int(args[0])
	primes = []
	while ((n % 2) == 0):
	    primes.append(2)
	    n //= 2
	x = 3
	while (n != 1):
	    while ((n % x) == 0):
	        primes.append(x)
	        n //= x
	    x += 2
	    if (x >= (math.floor(math.sqrt(n)) + 1)):
	        primes.append(n)
	        break
	factors = [1]
	for x in primes:
	    for y in factors[:]:
	        if (not ((x * y) in factors)):
	            factors.append((x * y))
	factors = sorted(factors)[::(- 1)]
	for x in factors:
	    condition = True
	    for y in range(2, (math.floor(math.sqrt(x)) + 1)):
	        if ((x % (y ** 2)) == 0):
	            condition = False
	            break
	    if condition:
	        ret_values.append(x)
	        break

	return ret_values
