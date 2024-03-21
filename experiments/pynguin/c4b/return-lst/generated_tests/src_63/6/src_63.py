def func(*args):
	ret_values = []
	
	a = int(args[0])
	x = 0
	div = []
	for i in range(1, (int((a ** 0.5)) + 1)):
	    if ((a % i) == 0):
	        div.append(i)
	b = len(div)
	for i in div[:b]:
	    div.append((a // i))
	div = list(set(div))
	for i in div:
	    t = 0
	    for j in str(i):
	        if (j in str(a)):
	            t = 1
	    x += t
	ret_values.append(x)

	return ret_values
