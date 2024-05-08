def original_func(*args):
	global_list = []
	
	
	def isLucky(n):
	    count = 0
	    while (n > 0):
	        r = (n % 10)
	        if ((r != 4) and (r != 7)):
	            count += 1
	            return False
	        n = (n // 10)
	    return True
	
	def numdig(n):
	    count = 0
	    while (n > 0):
	        r = (n % 10)
	        if ((r == 4) or (r == 7)):
	            count += 1
	        n = (n // 10)
	    return count
	n = int(args[0])
	if isLucky(numdig(n)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list