def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n <= 3):
	    if (n == 3):
	        mensaje = '7'
	    if (n == 2):
	        mensaje = '1'
	elif (n <= 7):
	    if (n == 4):
	        mensaje = '11'
	    if (n == 5):
	        mensaje = '71'
	    if (n == 6):
	        mensaje = '111'
	    if (n == 7):
	        mensaje = '711'
	else:
	    a = (n // 2)
	    if ((n % 2) == 0):
	        mensaje = ('1' * a)
	    else:
	        mensaje = ('7' + ('1' * (a - 1)))
	ret_values.append(mensaje)

	return ret_values
