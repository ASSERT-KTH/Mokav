def func(*args):
	
	
	def main():
	    from math import pi, sin
	    (n, R, r) = map(float, args[0].split())
	    return(('NO', 'YES')[((r * n) <= (R if (n < 3) else ((R * 2) if (n == 6) else (((R - r) * n) * sin((pi / n))))))])
	if (__name__ == '__main__'):
	    main()
