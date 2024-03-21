def func(*args):
	ret_values = []
	
	from math import ceil
	
	def calculNmbPave(n=0, m=0, a=0):
	    try:
	        l = int(ceil((n / a)))
	        h = int(ceil((m / a)))
	        return (h * l)
	    except ValueError:
	        ret_values.append('erreur de type')
	(n, m, a) = list(map(int, args[0].split()))
	ret_values.append(calculNmbPave(n, m, a))

	return ret_values
