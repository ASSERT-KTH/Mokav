def func(*args):
	
	
	def main():
	    (n, s) = map(int, args[0].split())
	    y = [i for i in range(s, (s + 180)) if ((i - sum([int(j) for j in str(i)])) >= s)]
	    a = y[0]
	    return(max(((n - a) + 1), 0))
	if (__name__ == '__main__'):
	    main()
