def original_func(*args):
	global_list = []
	
	
	def count_times(row):
	    res = (row != '')
	    hand = 0
	    n = len(row)
	    for i in range(1, n):
	        hand += 1
	        if ((hand == 3) or (row[i] != row[(i - 1)])):
	            hand = 0
	            res += 1
	    return res
	row = args[0]
	global_list.append(count_times(row))
	return global_list