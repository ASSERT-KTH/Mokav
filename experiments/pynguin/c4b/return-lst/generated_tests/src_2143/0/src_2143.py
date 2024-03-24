def func(*args):
	ret_values = []
	
	from math import sqrt
	from math import ceil
	
	def is_prime(number):
	    if (number == 2):
	        return True
	    for k in range(2, (ceil(sqrt(number)) + 1)):
	        if ((number % k) == 0):
	            return False
	    return True
	(n, k) = [int(x) for x in args[0].split()]
	prime_numbers = [x for x in range(2, (n + 1)) if is_prime(x)]
	answer = 0
	flag = 0
	if (k == 0):
	    ret_values.append('YES')
	else:
	    for i in range((len(prime_numbers) - 2)):
	        if (((prime_numbers[i] + prime_numbers[(i + 1)]) + 1) in prime_numbers):
	            answer += 1
	            if (answer == k):
	                ret_values.append('YES')
	                flag = 1
	                break
	    if (flag == 0):
	        ret_values.append('NO')

	return ret_values
