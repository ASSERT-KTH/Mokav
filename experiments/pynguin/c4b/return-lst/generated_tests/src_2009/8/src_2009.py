def func(*args):
	ret_values = []
	
	n = list(args[0])
	temp = ''.join(n)
	le = len(n)
	l = (len(n) // 2)
	if ((temp == temp[::(- 1)]) and ((le % 2) == 0)):
	    ret_values.append('NO')
	    exit()
	if ((temp == temp[::(- 1)]) and ((le % 2) != 0)):
	    ret_values.append('YES')
	    exit()
	if ((le % 2) == 0):
	    n1 = n[:l]
	    n2 = n[l:][::(- 1)]
	    c = 0
	    for i in list(zip(n1, n2)):
	        i = list(i)
	        if (i[0] != i[1]):
	            c = (c + 1)
	        if (c > 1):
	            ret_values.append('NO')
	            exit()
	    ret_values.append('YES')
	if ((le % 2) != 0):
	    n1 = n[:l]
	    n2 = n[(l + 1):][::(- 1)]
	    c = 0
	    for i in list(zip(n1, n2)):
	        i = list(i)
	        if (i[0] != i[1]):
	            c = (c + 1)
	        if (c > 1):
	            ret_values.append('NO')
	            exit()
	    ret_values.append('YES')

	return ret_values
