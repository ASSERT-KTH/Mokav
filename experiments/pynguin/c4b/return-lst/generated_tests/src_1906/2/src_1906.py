def func(*args):
	ret_values = []
	
	list = ['H', 'Q', '9']
	inputs = args[0]
	
	def Hqlang(inputs):
	    for i in inputs:
	        if (i in list):
	            return 'YES'
	    return 'NO'
	ret_values.append(Hqlang(inputs))

	return ret_values
