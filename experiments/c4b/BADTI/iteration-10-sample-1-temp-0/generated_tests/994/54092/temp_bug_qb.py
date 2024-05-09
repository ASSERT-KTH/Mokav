def original_func(*args):
	global_list = []
	
	
	def main(n, m, a):
	    width = (n % a)
	    length = (m % a)
	    return (width * length)
	(n, m, a) = map(int, args[0].split(' '))
	global_list.append(main(n, m, a))
	return global_list