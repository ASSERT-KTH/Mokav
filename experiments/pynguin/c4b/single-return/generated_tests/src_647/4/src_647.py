def func(*args):
	
	
	def main():
	    (a, b, c, d, e, f) = map(int, args[0].split())
	    if c:
	        c *= a
	        d *= b
	    if c:
	        c *= e
	        d *= f
	    return(('Hermione', 'Ron')[(c < d)])
	if (__name__ == '__main__'):
	    main()
