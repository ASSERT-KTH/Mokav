def func(*args):
	ret_values = []
	
	
	def isPrime(n):
	    i = 2
	    while ((i * i) <= n):
	        if ((n % i) == 0):
	            return False
	        i += 1
	    return True
	
	def main():
	    n = int(args[0])
	    if (isPrime(n) or (n == 2)):
	        ret_values.append(1)
	    elif (isPrime((n - 2)) or ((n % 2) == 0)):
	        ret_values.append(2)
	    else:
	        ret_values.append(3)
	main()

	return ret_values
