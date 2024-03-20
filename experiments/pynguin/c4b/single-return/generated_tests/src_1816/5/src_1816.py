def func(*args):
	
	lista = []
	resultado = []
	a = args[0]
	a = a.split(' ')
	lista.append(a)
	menor = 0
	tostadas = int((((int(a[1]) * int(a[2])) / int(a[(- 2)])) / int(a[0])))
	limas = int(((int(a[3]) * int(a[4])) / int(a[0])))
	sal = int(((int(a[5]) / int(a[(- 1)])) / int(a[0])))
	resultado.append(tostadas)
	resultado.append(limas)
	resultado.append(sal)
	for i in range(1, len(resultado)):
	    for j in range((len(resultado) - i)):
	        if (resultado[j] > resultado[(j + 1)]):
	            orden = resultado[j]
	            resultado[j] = resultado[(j + 1)]
	            resultado[(j + 1)] = orden
	return(resultado[0])
