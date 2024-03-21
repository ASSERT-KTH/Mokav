def func(*args):
	ret_values = []
	
	(n, a, b, c) = [int(n) for n in args[0].split()]
	tempN = n
	if ((tempN % 4) == 0):
	    ret_values.append(0)
	    quit()
	k = 1
	while True:
	    tempN += 1
	    if ((tempN % 4) == 0):
	        break
	    k += 1
	prices = []
	if (k == 1):
	    prices.append(a)
	    prices.append((c + b))
	    prices.append((3 * c))
	if (k == 2):
	    prices.append(b)
	    prices.append((2 * a))
	    prices.append((2 * c))
	if (k == 3):
	    prices.append(c)
	    prices.append((b + a))
	    prices.append((3 * a))
	ret_values.append(min(prices))

	return ret_values
