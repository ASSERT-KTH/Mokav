def original_func(*args):
	global_list = []
	
	import sys
	
	def isLucky(n):
	    for i in n:
	        if ((i != '4') and (i != '7')):
	            return False
	    return True
	a = str(args[0])
	drap = False
	if (isLucky(a) and isLucky(str(len(a)))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list