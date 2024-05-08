def original_func(*args):
	global_list = []
	
	import math
	
	def distancia_euclidiana(x, y):
	    lados = []
	    lados.append(math.sqrt((math.pow((x[0] - x[1]), 2) + math.pow((y[0] - y[1]), 2))))
	    lados.append(math.sqrt((math.pow((x[0] - x[2]), 2) + math.pow((y[0] - y[2]), 2))))
	    lados.append(math.sqrt((math.pow((x[1] - x[2]), 2) + math.pow((y[1] - y[2]), 2))))
	    return sorted(lados)
	
	def is_right(pontos):
	    distancias = distancia_euclidiana((pontos[0], pontos[2], pontos[4]), (pontos[1], pontos[3], pontos[5]))
	    return ((distancias[0] > 0) and (distancias[2] == (distancias[1] + distancias[0])))
	pontos = [int(i) for i in args[0].split()]
	resultado = 'NEITHER'
	if is_right(pontos):
	    resultado = 'RIGHT'
	else:
	    for i in range(0, 6):
	        pontos[i] += 1
	        if is_right(pontos):
	            resultado = 'ALMOST'
	            break
	        pontos[i] -= 2
	        if is_right(pontos):
	            resultado = 'ALMOST'
	            break
	        pontos[i] += 1
	global_list.append(resultado)
	return global_list