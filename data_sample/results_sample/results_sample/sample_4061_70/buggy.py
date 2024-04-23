def func(*args):
	
	M = [args[0] for i in range(8)]
	l = []
	p = 100000000
	for i in range(8):
	    for j in range(8):
	        if ((M[i][j] == 'W') and (j not in l)):
	            p = i
	            break
	        if (M[i][j] == 'B'):
	            l.append(j)
	    if (p != 100000000):
	        break
	l = []
	for i in range(7, (- 1), (- 1)):
	    for j in range(7, (- 1), (- 1)):
	        if ((M[i][j] == 'B') and (j not in l)):
	            if (p < ((8 - i) - 1)):
	                yield('A')
	            else:
	                yield('B')
	            exit()
	        if (M[i][j] == 'W'):
	            l.append(j)
	yield('A')
