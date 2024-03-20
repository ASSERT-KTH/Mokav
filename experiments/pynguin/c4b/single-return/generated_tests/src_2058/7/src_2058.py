def func(*args):
	
	(n, k) = map(int, args[0].split())
	chars_dis = (((n // k) + 1) * [chr((i + 97)) for i in range(k)])
	return(''.join(chars_dis[:n]))
