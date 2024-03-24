def func(*args):
	
	
	def main():
	    mode = 'filee'
	    if (mode == 'file'):
	        f = open('test.txt', 'r')
	    get = (lambda : [int(x) for x in (f.readline() if (mode == 'file') else args[0]).split()])
	    [a, b, r] = get()
	    return(('First' if (min(a, b) >= (2 * r)) else 'Second'))
	    if (mode == 'file'):
	        f.close()
	if (__name__ == '__main__'):
	    main()
