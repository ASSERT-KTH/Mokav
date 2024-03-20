def func(*args):
	
	list = ['H', 'Q', '9']
	inputs = args[0]
	
	def Hqlang(inputs):
	    for i in inputs:
	        if (i in list):
	            return 'YES'
	    return 'NO'
	return(Hqlang(inputs))
