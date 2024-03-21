def func(*args):
	ret_values = []
	
	'\n\tAuthor\t\t: Arif Ahmad\n\tDate  \t\t: \n\tAlgo  \t\t: \n\tDifficulty\t: \n'
	
	def main():
	    (n, R, r) = map(int, args[0].split())
	    if (n == 1):
	        if (r <= R):
	            ret_values.append('YES')
	        else:
	            ret_values.append('NO')
	    else:
	        import math
	        a = ((R - r) * math.sin((math.pi / n)))
	        if (r < (a + 1e-07)):
	            ret_values.append('YES')
	        else:
	            ret_values.append('NO')
	if (__name__ == '__main__'):
	    main()

	return ret_values
