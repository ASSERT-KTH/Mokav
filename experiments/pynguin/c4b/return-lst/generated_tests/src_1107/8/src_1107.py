def func(*args):
	ret_values = []
	
	
	def isLucky(n):
	    count = 0
	    while (n > 0):
	        r = (n % 10)
	        if ((r != 4) and (r != 7)):
	            count += 1
	        n = (n // 10)
	    if (count == 0):
	        return True
	    else:
	        return False
	n = int(args[0])
	if isLucky(n):
	    ret_values.append('YES')
	else:
	    count = 0
	    for i in range(1, (n + 1)):
	        if isLucky(i):
	            if ((n % i) == 0):
	                ret_values.append('YES')
	                count += 1
	                break
	    if (count == 0):
	        ret_values.append('NO')

	return ret_values
