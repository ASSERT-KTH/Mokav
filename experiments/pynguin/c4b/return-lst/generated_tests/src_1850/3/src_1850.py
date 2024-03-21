def func(*args):
	ret_values = []
	
	import math
	
	def divisorGenerator(n):
	    large_divisors = []
	    for i in range(1, int((math.sqrt(n) + 1))):
	        if ((n % i) == 0):
	            (yield i)
	            if ((i * i) != n):
	                large_divisors.append((n / i))
	    for divisor in reversed(large_divisors):
	        (yield divisor)
	(n, k) = list(map(int, args[0].strip().split(' ')))
	l = list(map(int, divisorGenerator(n)))
	lenght = (len(l) - 1)
	flag = True
	while (lenght >= 0):
	    p = l[lenght]
	    if (((p * int((n / p))) == n) and (k <= (int((n / p)) - int(((k * (k - 1)) / 2))))):
	        for i in range(1, k):
	            ret_values.append((p * i), end=' ')
	        ret_values.append((p * (int((n / p)) - int(((k * (k - 1)) / 2)))))
	        flag = False
	        break
	    lenght -= 1
	if flag:
	    ret_values.append((- 1))

	return ret_values
