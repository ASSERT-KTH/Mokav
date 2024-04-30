def original_func(*args):
	global_list = []
	
	(x, y) = args[0].split()
	Vladik = int(x)
	Valera = int(y)
	i = 1
	while ((Vladik != 0) or (Valera != 0)):
	    Vladik = (Vladik - i)
	    if (Vladik < 0):
	        global_list.append('Vladik')
	        break
	    i = (i + 1)
	    Valera = (Valera - i)
	    if (Valera < 0):
	        global_list.append('Valera')
	        break
	    i = (i + 1)
	return global_list