def func(*args):
	ret_values = []
	
	import os
	import string
	(n, k) = map(int, args[0].split())
	use = string.ascii_lowercase[:k]
	for i in range(n):
	    ret_values.append(use[(i % k)], end='')
	ret_values.append()
	if (os.getlogin() == 'o.sharipov'):
	    args[1]

	return ret_values
