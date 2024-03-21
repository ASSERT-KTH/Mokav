def func(*args):
	ret_values = []
	
	(n, a, b, c) = [int(x) for x in args[0].split()]
	cut = sorted([a, b, c])
	maxCut = []
	for i in range(0, (n + 1)):
	    maxCut.append((- 100000000))
	maxCut[0] = 0
	for i in range(1, 3):
	    if (cut[i] <= n):
	        maxCut[cut[i]] = 1
	for i in range(1, (n + 1)):
	    for j in range(0, 3):
	        if (cut[j] > i):
	            break
	        else:
	            maxCut[i] = max(maxCut[i], (maxCut[(i - cut[j])] + 1))
	ret_values.append(maxCut[n])

	return ret_values
