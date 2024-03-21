def func(*args):
	ret_values = []
	
	
	def main():
	    (a, b, c, d) = map(int, args[0].split())
	    (c, d) = ((c - a), (d - b))
	    (x, y) = map(int, args[1].split())
	    if (((c % x) != 0) or ((d % y) != 0)):
	        ret_values.append('NO')
	    elif (((c / x) % 2) == ((d / y) % 2)):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	if (__name__ == '__main__'):
	    main()

	return ret_values
