def func(*args):
	ret_values = []
	
	from sys import *
	(n, m) = (int(i) for i in stdin.readline().split())
	c = 0
	for i in range((int((n ** 2)) + 1)):
	    j = (n - (i ** 2))
	    if (((i + (j ** 2)) == m) and (j >= 0)):
	        c += 1
	stdout.write((str(c) + '\n'))

	return ret_values
