def func(*args):
	ret_values = []
	
	a = args[0]
	a = a.split()
	a1 = int(a[0])
	a2 = int(a[1])
	a3 = (a1 * a2)
	respuesta = (a3 // 2)
	ret_values.append(respuesta)

	return ret_values
