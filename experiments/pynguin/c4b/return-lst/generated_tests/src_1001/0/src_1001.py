def func(*args):
	ret_values = []
	
	
	def gcd(num1, num2):
	    i = min(num1, num2)
	    while (i > 0):
	        if (((num1 % i) == 0) and ((num2 % i) == 0)):
	            return i
	        i -= 1
	if (__name__ == '__main__'):
	    [a, b, n] = [int(x) for x in args[0].split()]
	    turn = 's'
	    while True:
	        if (turn == 's'):
	            simon = gcd(a, n)
	            if ((simon is not None) and ((n - simon) >= 0)):
	                n -= simon
	                turn = 'a'
	            else:
	                ret_values.append('1')
	                exit()
	        else:
	            anti_simon = gcd(b, n)
	            if ((anti_simon is not None) and ((n - anti_simon) >= 0)):
	                n -= anti_simon
	                turn = 's'
	            else:
	                ret_values.append('0')
	                exit()

	return ret_values
