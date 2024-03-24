def func(*args):
	
	a = args[0]
	a = a.split()
	a1 = int(a[0])
	a2 = int(a[1])
	a3 = (a1 * a2)
	respuesta = (a3 // 2)
	return(respuesta)
