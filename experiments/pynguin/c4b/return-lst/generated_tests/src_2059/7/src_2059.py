def func(*args):
	ret_values = []
	
	
	def main(n, m, a):
	    width = ((n // a) + ((n % a) > 0))
	    length = ((m // a) + ((m % a) > 0))
	    return (width * length)
	(n, m, a) = map(int, args[0].split(' '))
	ret_values.append(main(n, m, a))

	return ret_values
