def original_func(*args):
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
	entrada = args[0]
	numero = contador(entrada)
	if (numero[0] == numero[1]):
	    global_list.append(entrada.lower())
	if ((numero[0] == len(entrada)) or (numero[1] == len(entrada))):
	    global_list.append(entrada)
	if (numero[0] > numero[1]):
	    global_list.append(entrada.upper())
	if (numero[0] < numero[1]):
	    global_list.append(entrada.lower())
	return global_list