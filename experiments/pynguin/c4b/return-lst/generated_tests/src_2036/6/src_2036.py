def func(*args):
	ret_values = []
	
	from sys import stdin, stdout
	
	def check(m, k):
	    for i in range(2, (int((m ** 0.5)) + 1)):
	        if ((not (m % i)) and ((i >= k) or ((m // i) >= k))):
	            return 1
	    else:
	        return 0
	(n, m, k) = map(int, stdin.readline().split())
	if ((m < (2 * k)) or ((k != 1) and (not check(m, k)))):
	    stdout.write('Marsel')
	elif (n % 2):
	    stdout.write('Timur')
	else:
	    stdout.write('Marsel')

	return ret_values
