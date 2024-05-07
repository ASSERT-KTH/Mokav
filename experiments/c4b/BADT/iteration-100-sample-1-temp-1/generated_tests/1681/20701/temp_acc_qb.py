def patched_func(*args):
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
	(n, m) = get_int()
	ans = 0
	for i in range((n + 1)):
	    for j in range((m + 1)):
	        if ((((i ** 2) + j) == n) and ((i + (j ** 2)) == m)):
	            ans += 1
	global_list.append(ans)
	return global_list