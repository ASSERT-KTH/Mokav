def original_func(*args):
	global_list = []
	
	import math
	
	def doubleCola(n):
	    sum = 0
	    i = 0
	    while (sum < n):
	        sum += (5 * (2 ** i))
	        i += 1
	    sum -= (5 * (2 ** (i - 1)))
	    if (sum > 0):
	        n -= sum
	    which = 1
	    while ((n - i) > 0):
	        n -= (2 ** i)
	        which += 1
	    nameDict = {1: 'Sheldon', 2: 'Leonard', 3: 'Penny', 4: 'Rajesh', 5: 'Howard'}
	    return nameDict[which]
	global_list.append(doubleCola(int(args[0])))
	return global_list