def func(*args):
	
	import math
	
	def bigBear(a, b):
	    yearWithFloat = (math.log((b / a)) / math.log(1.5))
	    year = math.ceil(yearWithFloat)
	    return (year if (year > yearWithFloat) else (year + 1))
	(a, b) = map(float, args[0].split())
	return(bigBear(a, b))
