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
	(a1, a2) = get_int()
	ans = 0
	while ((a1 > 0) and (a2 > 0) and ((a1 != 1) or (a2 != 1))):
	    ans += 1
	    if (a2 > a1):
	        a1 += 1
	        a2 -= 2
	    else:
	        a2 += 1
	        a1 -= 2
	global_list.append(ans)
	return global_list