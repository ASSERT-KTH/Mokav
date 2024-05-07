def original_func(*args):
	global_list = []
	
	year = int(args[0])
	unique = False
	
	def checkUnique(year):
	    checkList = []
	    for c in str(year):
	        if (c in checkList):
	            return False
	        checkList.append(c)
	    return True
	while (not unique):
	    if checkUnique(year):
	        unique = True
	    year += 1
	global_list.append(year)
	return global_list