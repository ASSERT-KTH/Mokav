def func(*args):
	ret_values = []
	
	(pontoAx, pontoAy) = [int(i) for i in args[0].split()]
	(pontoBx, pontoBy) = [int(i) for i in args[1].split()]
	(pontoCx, pontoCy) = [int(i) for i in args[2].split()]
	(x4, x5) = ((pontoBx - pontoAx), (pontoCx - pontoBx))
	(y4, y5) = ((pontoBy - pontoAy), (pontoCy - pontoBy))
	direcao = ((x4 * y5) - (x5 * y4))
	if (direcao > 0):
	    ret_values.append('LEFT')
	elif (direcao < 0):
	    ret_values.append('RIGHT')
	else:
	    ret_values.append('TOWARDS')

	return ret_values
