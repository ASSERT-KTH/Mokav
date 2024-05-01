def patched_func(*args):
	global_list = []
	
	list = ['H', 'Q', '9']
	inputs = args[0]
	
	def Hqlang(inputs):
	    for i in inputs:
	        if (i in list):
	            return 'YES'
	    return 'NO'
	global_list.append(Hqlang(inputs))
	return global_list