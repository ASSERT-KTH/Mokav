def func(*args):
	ret_values = []
	
	(x, y) = args[0].split()
	Vladik = int(x)
	Valera = int(y)
	i = 1
	while True:
	    Vladik = (Vladik - i)
	    if (Vladik < 0):
	        ret_values.append('Vladik')
	        break
	    i = (i + 1)
	    Valera = (Valera - i)
	    if (Valera < 0):
	        ret_values.append('Valera')
	        break
	    i = (i + 1)

	return ret_values
