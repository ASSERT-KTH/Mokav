def func(*args):
	ret_values = []
	
	
	def main():
	    (a, b, c, d, e, f) = map(int, args[0].split())
	    if c:
	        c *= a
	        d *= b
	    if c:
	        c *= e
	        d *= f
	    ret_values.append(('Hermione', 'Ron')[(c < d)])
	if (__name__ == '__main__'):
	    main()

	return ret_values
