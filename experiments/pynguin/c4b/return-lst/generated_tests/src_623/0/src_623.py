def func(*args):
	ret_values = []
	
	letter = [chr((ord('a') + i)) for i in range(26)]
	(n, k) = [int(i) for i in args[0].split()]
	if ((k > n) or ((k == 1) and (n > 1))):
	    ret_values.append((- 1))
	    exit()
	if (k == 1):
	    ret_values.append('a')
	    exit()
	ans = [letter[(i % 2)] for i in range(((n - k) + 2))]
	ans += [letter[(2 + i)] for i in range((k - 2))]
	ret_values.append(''.join(ans))

	return ret_values
