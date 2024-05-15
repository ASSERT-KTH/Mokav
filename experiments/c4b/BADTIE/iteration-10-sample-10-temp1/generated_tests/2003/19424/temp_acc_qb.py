def patched_func(*args):
	global_list = []
	
	
	def isDistinct(year):
	    for i in range(0, 4):
	        for j in range(0, 4):
	            if (i != j):
	                if (year[i] == year[j]):
	                    return False
	    return True
	year = int(args[0])
	for i in range((year + 1), 100000):
	    if isDistinct(str(i)):
	        global_list.append(i)
	        break
	return global_list