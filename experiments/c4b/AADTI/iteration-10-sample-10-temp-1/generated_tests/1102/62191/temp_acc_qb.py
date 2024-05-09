def patched_func(*args):
	global_list = []
	
	entrada = str(args[0])
	entrada = entrada.lower()
	letras = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
	entrada = entrada.replace('a', '')
	entrada = entrada.replace('e', '')
	entrada = entrada.replace('i', '')
	entrada = entrada.replace('o', '')
	entrada = entrada.replace('u', '')
	entrada = entrada.replace('y', '')
	saida = ''
	for letra in entrada:
	    if (letra in letras):
	        saida += ('.' + letra)
	global_list.append(saida)
	return global_list