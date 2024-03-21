def func(*args):
	ret_values = []
	
	a = int(args[0])
	a //= 2
	n = args[1]
	results = 'NO'
	condition = True
	for x in n:
	    if ((x != '4') and (x != '7')):
	        condition = False
	        break
	if condition:
	    x = sum(map(int, list(n[:a])))
	    y = sum(map(int, list(n[a:])))
	    if (x == y):
	        results = 'YES'
	ret_values.append(results)

	return ret_values
