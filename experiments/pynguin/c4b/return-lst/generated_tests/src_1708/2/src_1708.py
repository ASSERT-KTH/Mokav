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
	(n, k) = [int(i) for i in args[0].split()]
	numbers = list(sieve(n))
	ans = 0
	for i in range(5, len(numbers)):
	    current = (numbers[i] - 1)
	    for idx2 in range(0, i):
	        if (idx2 == (i - 1)):
	            break
	        if ((numbers[idx2] + numbers[(idx2 + 1)]) == current):
	            ans += 1
	if (ans >= k):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
