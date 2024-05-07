def patched_func(*args):
	global_list = []
	
	
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
	        global_list.append(1)
	    elif (isPrime((n - 2)) or ((n % 2) == 0)):
	        global_list.append(2)
	    else:
	        global_list.append(3)
	main()
	return global_list