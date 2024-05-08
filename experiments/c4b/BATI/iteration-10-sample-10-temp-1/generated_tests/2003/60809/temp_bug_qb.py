def original_func(*args):
	global_list = []
	
	n = int(args[0])
	
	def are_digits_distinct(num):
	    num_as_str = str(num)
	    for i in range((len(num_as_str) - 1)):
	        cur = num_as_str[i]
	        for j in range((i + 1), len(num_as_str)):
	            if (cur == num_as_str[j]):
	                return False
	    return True
	for num in range((n + 1), 9001):
	    if are_digits_distinct(num):
	        global_list.append(num)
	        break
	return global_list