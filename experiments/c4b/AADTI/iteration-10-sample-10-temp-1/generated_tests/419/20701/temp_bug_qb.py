def original_func(*args):
	global_list = []
	
	import math
	
	def get_primes(prime_supr):
	    is_prime = (([0] * 2) + ([1] * prime_supr))
	    for i in range(2, (int(math.sqrt(prime_supr)) + 1)):
	        if is_prime[i]:
	            for j in range((i * i), (prime_supr + 1), i):
	                is_prime[j] = 0
	    return is_prime
	get_int = (lambda : map(int, args[0].split()))
	(n, a, b) = get_int()
	ans = ([n] + [i for i in range(n)])
	global_list.append(ans[((a + b) % n)])
	return global_list