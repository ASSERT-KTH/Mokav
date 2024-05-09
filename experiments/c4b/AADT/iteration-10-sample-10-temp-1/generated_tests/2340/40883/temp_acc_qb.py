def patched_func(*args):
	global_list = []
	
	import string
	minuscula = string.ascii_lowercase
	mayuscula = string.ascii_uppercase
	
	def contador(entrada):
	    cont_may = 0
	    for i in range(len(entrada)):
	        if (not (entrada[i] in minuscula)):
	            cont_may += 1
	    cont_min = (len(entrada) - cont_may)
	    return (cont_may, cont_min)
	
	def juego(num):
	    if (num[0] == num[1]):
	        return entrada.lower()
	    if ((num[0] == len(entrada)) or (num[1] == len(entrada))):
	        return entrada
	    if (num[0] > num[1]):
	        return entrada.upper()
	    if (num[0] < num[1]):
	        return entrada.lower()
	entrada = args[0]
	numero = contador(entrada)
	global_list.append(juego(numero))
	return global_list