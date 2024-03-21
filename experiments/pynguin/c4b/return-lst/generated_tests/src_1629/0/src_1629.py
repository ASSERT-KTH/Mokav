def func(*args):
	ret_values = []
	
	
	def main():
	    n = int(args[0])
	    p = funct(n)
	    if (p == 1):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	
	def funct(n):
	    a = 0
	    while (a <= n):
	        b = 0
	        while (b <= (n - a)):
	            if ((((n - a) - b) % 1234) == 0):
	                return 1
	            else:
	                b += 123456
	        a += 1234567
	    return 0
	main()

	return ret_values
