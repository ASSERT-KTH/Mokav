def func(*args):
	ret_values = []
	
	
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
	        ret_values.append(i)
	        break

	return ret_values
