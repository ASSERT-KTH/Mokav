def original_func(*args):
	global_list = []
	
	x = args[0]
	
	def hm(x):
	    if (len(x) == 1):
	        return x
	    elif ((len(x) == 2) and (x[1] == '8')):
	        return x
	    elif ((x[1:(- 1)] == ('9' * (len(x) - 2))) and (x[(- 1)] in ('8', '9'))):
	        return x
	    else:
	        return (hm(str((int(x[:(- 1)]) - 1))) + '9')
	global_list.append(int(hm(x)))
	return global_list