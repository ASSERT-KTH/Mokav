def original_func(*args):
	global_list = []
	
	entrada = args[0].lower()
	entrada = entrada.replace('a', '')
	entrada = entrada.replace('e', '')
	entrada = entrada.replace('i', '')
	entrada = entrada.replace('o', '')
	entrada = entrada.replace('u', '')
	entrada.split()
	i = 2
	final = ''
	for j in entrada:
	    if (i == 2):
	        final += '.'
	        i = 1
	    final += j
	    i += 1
	global_list.append(final)
	return global_list