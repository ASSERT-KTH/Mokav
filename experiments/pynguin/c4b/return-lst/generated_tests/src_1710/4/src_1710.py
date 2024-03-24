def func(*args):
	ret_values = []
	
	
	def sieve(n):
	    np1 = (n + 1)
	    s = list(range(np1))
	    s[1] = 0
	    sqrtn = int(round((n ** 0.5)))
	    for i in range(2, (sqrtn + 1)):
	        if s[i]:
	            s[(i * i):np1:i] = ([0] * len(range((i * i), np1, i)))
	    return filter(None, s)
	n = int(args[0])
	numbers = list(sieve(n))
	answer = 0
	for i in range(6, (n + 1)):
	    counter = 0
	    for prime in numbers:
	        if ((i % prime) == 0):
	            counter += 1
	        if ((counter > 2) or (prime > i)):
	            break
	    if (counter == 2):
	        answer += 1
	ret_values.append(answer)

	return ret_values
