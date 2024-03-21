def func(*args):
	ret_values = []
	
	entrada = str(args[0])
	cont1 = 0
	cont2 = 0
	maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	tamanho = len(entrada)
	for i in entrada:
	    if (i in maiusculas):
	        cont1 += 1
	if (cont1 == tamanho):
	    saida = entrada[0:].lower()
	    ret_values.append(saida)
	elif (entrada[0] in maiusculas):
	    ret_values.append(entrada)
	else:
	    for j in entrada:
	        if (j in minusculas):
	            cont2 += 1
	    if (cont2 <= 1):
	        saida = entrada[0].upper()
	        saida += entrada[1:].lower()
	        ret_values.append(saida)
	    else:
	        ret_values.append(entrada)

	return ret_values
