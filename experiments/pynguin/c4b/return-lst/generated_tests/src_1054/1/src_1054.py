def func(*args):
	ret_values = []
	
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
	if (suma >= a):
	    ret_values.append(cont)
	else:
	    ret_values.append((- 1))

	return ret_values
