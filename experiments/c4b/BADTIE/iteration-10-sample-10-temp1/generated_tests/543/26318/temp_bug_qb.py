def original_func(*args):
	global_list = []
	
	
	def main():
	    n = int(args[0])
	    p = original_funct(n)
	    if (p == 1):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	
	def original_funct(n):
	    a = 0
	    while (a <= n):
	        b = 0
	        while (b <= (n - a)):
	            if ((((n - a) - b) % 1234) == 0):
	                global_list.append('True')
	                return 1
	            else:
	                b += 123456
	        a += 1234567
	    return 0
	main()
	return global_list