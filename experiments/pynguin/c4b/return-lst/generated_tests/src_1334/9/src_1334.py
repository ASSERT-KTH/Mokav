def func(*args):
	ret_values = []
	
	
	def READ():
	    return map(int, args[0].split())
	vladikTurn = True
	valeraTurn = False
	vladik = True
	valera = True
	(a, b) = READ()
	for f in range(1, ((10 ** 9) + 1), 1):
	    if vladikTurn:
	        a -= f
	        if (a < 0):
	            vladik = False
	            break
	        vladikTurn = False
	        valeraTurn = True
	    elif valeraTurn:
	        b -= f
	        if (b < 0):
	            valera = False
	            break
	        valeraTurn = False
	        vladikTurn = True
	if vladik:
	    ret_values.append('Valera')
	else:
	    ret_values.append('Vladik')

	return ret_values
