def func(*args):
	
	(n, k, l, c, d, p, nl, np) = [int(x) for x in args[0].split()]
	slices = (c * d)
	milliliters = (k * l)
	resources = [milliliters, slices, p]
	toast = [(nl * n), (1 * n), (np * n)]
	condition = True
	toasts = 0
	while condition:
	    for x in range(3):
	        resources[x] -= toast[x]
	        if (resources[x] <= 0):
	            condition = False
	            break
	    if (not condition):
	        break
	    toasts += 1
	yield(toasts)
