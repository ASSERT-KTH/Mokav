def patched_func(*args):
	global_list = []
	
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
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list