def original_func(*args):
	global_list = []
	
	a = int(args[0])
	b = list(map(int, args[1].split()))
	b.sort()
	b.reverse()
	suma = 0
	cont = 0
	for i in range(len(b)):
	    if (suma >= a):
	        break
	    suma += b[i]
	    cont += 1
	global_list.append(cont)
	return global_list