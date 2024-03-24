def func(*args):
	ret_values = []
	
	
	def isUnique(strYear):
	    numbers = '0123456789'
	    uniques = 0
	    for num in numbers:
	        if strYear.__contains__(num):
	            uniques += 1
	    return (uniques == 4)
	year = int(args[0])
	for y in range((year + 1), 10000):
	    if isUnique(str(y)):
	        ret_values.append(y)
	        break

	return ret_values
