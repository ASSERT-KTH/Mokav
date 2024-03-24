def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    (n, k) = map(int, args[0].split())
	    prime = [2]
	    for i in range(3, (n + 1)):
	        i_is_prime = True
	        for j in range(2, (int((i ** 0.5)) + 1)):
	            if ((i % j) == 0):
	                i_is_prime = False
	                break
	        if i_is_prime:
	            prime.append(i)
	    count = 0
	    for i in prime:
	        for j in range(len(prime)):
	            if (prime[j] < int((i / 2))):
	                if (((prime[j] + prime[(j + 1)]) + 1) == i):
	                    count += 1
	                    break
	            else:
	                break
	    if (count >= k):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
