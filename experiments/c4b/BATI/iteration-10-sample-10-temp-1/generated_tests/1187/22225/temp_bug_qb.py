def original_func(*args):
	global_list = []
	
	a = args[0]
	a = ' '.join(a)
	a = a.split()
	suma = 0
	entra = 0
	for k in range(len(a)):
	    if (a[k] == a[k].upper()):
	        suma = (suma + 1)
	    elif (k == 0):
	        entra = 1
	if ((suma == len(a)) or ((suma == (len(a) - 1)) and (entra == 1))):
	    a[0] = a[0].upper()
	    for k in range(1, len(a)):
	        a[k] = a[k].lower()
	    mensaje = ''.join(a)
	else:
	    mensaje = ''.join(a)
	global_list.append(mensaje)
	return global_list