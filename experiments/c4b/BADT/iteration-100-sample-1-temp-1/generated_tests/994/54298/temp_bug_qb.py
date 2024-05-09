def original_func(*args):
	global_list = []
	
	from math import ceil
	
	def calculNmbPave(n=0, m=0, a=0):
	    try:
	        l = int(ceil((n / a)))
	        h = int(ceil((m / a)))
	        return (h * l)
	    except ValueError:
	        global_list.append('erreur de type')
	global_list.append(calculNmbPave(6, 6, 4))
	return global_list