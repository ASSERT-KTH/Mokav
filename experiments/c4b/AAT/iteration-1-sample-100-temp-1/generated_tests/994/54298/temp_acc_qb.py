def patched_func(*args):
	global_list = []
	
	from math import ceil
	
	def calculNmbPave(n=0, m=0, a=0):
	    try:
	        l = int(ceil((n / a)))
	        h = int(ceil((m / a)))
	        return (h * l)
	    except ValueError:
	        global_list.append('erreur de type')
	(n, m, a) = list(map(int, args[0].split()))
	global_list.append(calculNmbPave(n, m, a))
	return global_list