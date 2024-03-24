def func(*args):
	
	entrada = (int(args[0]) - 1)
	suma = 0
	nombres = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	for i in range(30):
	    a = (5 * (2 ** i))
	    suma += a
	    if (entrada < suma):
	        b = int(((entrada - (suma - (5 * (2 ** i)))) / (2 ** i)))
	        break
	return(nombres[b])
