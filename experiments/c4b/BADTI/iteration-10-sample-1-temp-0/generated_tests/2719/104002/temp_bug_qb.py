def original_func(*args):
	global_list = []
	
	import math
	
	def bigBear(a, b):
	    a = (a * 1.0)
	    b = (b * 1.0)
	    yearWithFloat = (math.log((b / a)) / math.log(1.5))
	    year = math.ceil(yearWithFloat)
	    return (year if (year > yearWithFloat) else (year + 1))
	global_list.append(bigBear(1, 1))
	global_list.append(bigBear(4, 9))
	global_list.append(bigBear(4, 7))
	return global_list