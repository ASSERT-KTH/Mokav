def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	chars_dis = (((n // k) + 1) * [chr((i + 97)) for i in range(k)])
	ret_values.append(''.join(chars_dis[:n]))

	return ret_values
