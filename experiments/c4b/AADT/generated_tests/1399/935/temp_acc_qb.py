def patched_func(*args):
	global_list = []
	
	import math
	prime = [2]
	
	def isPrime(arg):
	    flag = True
	    for i in range(3, (arg + 1)):
	        for j in range(2, ((i // 2) + 1)):
	            if ((i % j) == 0):
	                flag = False
	                break
	        if flag:
	            prime.append(i)
	        flag = True
	(n, k) = map(int, args[0].split())
	isPrime(n)
	count = 0
	for i in range(len(prime)):
	    for j in range((len(prime) - 1)):
	        if (((prime[j] + prime[(j + 1)]) + 1) == prime[i]):
	            count += 1
	if (count >= k):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list