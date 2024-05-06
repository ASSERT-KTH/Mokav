def patched_func(*args):
	global_list = []
	
	MAX = 50
	primes = []
	for i in range(2, (MAX + 1)):
	    prime = True
	    for j in range(2, i):
	        if ((i % j) == 0):
	            prime = False
	    if prime:
	        primes.append(i)
	(n, m) = list(map(int, args[0].split()))
	en = primes.index(n)
	em = (- 1)
	if (m in primes):
	    em = primes.index(m)
	if (en == (em - 1)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list