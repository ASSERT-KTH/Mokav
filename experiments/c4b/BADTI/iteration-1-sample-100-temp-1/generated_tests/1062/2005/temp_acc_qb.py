def patched_func(*args):
	global_list = []
	
	
	def nln(s):
	    numList = ['4', '7']
	    luckyCount = 0
	    for char in str(s):
	        if (char in numList):
	            luckyCount += 1
	    if isLucky(luckyCount):
	        return 'YES'
	    return 'NO'
	
	def isLucky(n):
	    numList = ['4', '7']
	    for char in str(n):
	        if (char not in numList):
	            return False
	    return True
	global_list.append(nln(args[0]))
	return global_list