def original_func(*args):
	global_list = []
	
	x = args[0]
	x = ' '.join(x)
	x = x.split()
	y = 0
	na = 8
	suma = 0
	mensaje = 'NO'
	for s in range((len(x) - 7)):
	    for m in range((s + 1), (s + 8)):
	        if (x[s] == x[m]):
	            na = 9
	            break
	        suma = (suma + 1)
	        if (suma == 7):
	            break
	    if (suma == 7):
	        mensaje = 'YES'
	        break
	    suma = 0
	global_list.append(mensaje)
	return global_list