def func(*args):
	ret_values = []
	
	l = [int(x) for x in args[0].split()]
	l.sort()
	(b, a) = l
	s1 = list(bin(a)[2:])
	s2 = list(bin(b)[2:])
	if (s1 == s2):
	    ret_values.append(0)
	elif (len(s1) == len(s2)):
	    cont = 0
	    while (s1[cont] == s2[cont]):
	        s1[cont] = '0'
	        cont += 1
	    for i in range(cont, len(s1)):
	        s1[i] = '1'
	    ret_values.append(int(''.join(s1), 2))
	else:
	    for i in range(len(s1)):
	        s1[i] = '1'
	    ret_values.append(int(''.join(s1), 2))

	return ret_values
