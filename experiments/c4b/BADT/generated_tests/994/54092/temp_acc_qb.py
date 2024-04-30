def patched_func(*args):
	global_list = []
	
	
	def main(n, m, a):
	    width = ((n // a) + ((n % a) > 0))
	    length = ((m // a) + ((m % a) > 0))
	    return (width * length)
	(n, m, a) = map(int, args[0].split(' '))
	global_list.append(main(n, m, a))
	return global_list