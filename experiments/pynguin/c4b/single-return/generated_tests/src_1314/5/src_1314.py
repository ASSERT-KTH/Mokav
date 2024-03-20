def func(*args):
	
	
	def main():
	    x = int(args[0])
	    return(jumps(x))
	
	def jumps(n):
	    n = abs(n)
	    i = 0
	    while True:
	        product = ((i * (i + 1)) // 2)
	        if ((product >= n) and ((product % 2) == (n % 2))):
	            return i
	        i += 1
	main()
