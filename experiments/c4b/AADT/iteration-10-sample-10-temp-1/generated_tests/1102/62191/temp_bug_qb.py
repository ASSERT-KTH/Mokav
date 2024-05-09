def original_func(*args):
	global_list = []
	
	entrada = str(args[0])
	entrada = entrada.lower()
	vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	saida = '.'
	for letra in entrada:
	    if (letra not in vogais):
	        saida += (letra + '.')
	saida = saida[:(- 1)]
	global_list.append(saida)
	return global_list