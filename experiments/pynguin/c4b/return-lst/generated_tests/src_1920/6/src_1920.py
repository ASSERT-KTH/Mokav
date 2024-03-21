def func(*args):
	ret_values = []
	
	prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
	num = [int(i) for i in args[0].split()]
	if (prime[(prime.index(num[0]) + 1)] == num[1]):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
