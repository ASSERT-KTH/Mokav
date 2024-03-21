def func(*args):
	ret_values = []
	
	import sys
	
	def isLucky(n):
	    for i in n:
	        if ((i != '4') and (i != '7')):
	            return False
	    return True
	
	def nearlyLucky(n):
	    count = 0
	    for i in n:
	        if ((i == '4') or (i == '7')):
	            count = (count + 1)
	    return count
	a = str(args[0])
	drap = False
	if isLucky(str(nearlyLucky(a))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
