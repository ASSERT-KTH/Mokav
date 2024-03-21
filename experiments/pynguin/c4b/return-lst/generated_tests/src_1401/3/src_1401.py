def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split(' '))
	nums = []
	for i in range(0, k):
	    nums.append((n - i))
	for i in range(1, ((n - k) + 1)):
	    nums.append(i)
	ret_values.append(' '.join(map(str, nums)))

	return ret_values
