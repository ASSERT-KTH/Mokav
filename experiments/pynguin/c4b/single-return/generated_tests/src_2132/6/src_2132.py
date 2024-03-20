def func(*args):
	
	inp = args[0]
	lista = list()
	keyList = list()
	ans = 0
	maxLen = 0
	occ = dict()
	for x1 in range(len(inp)):
	    for x2 in range(x1, len(inp)):
	        substr = inp[x1:(x2 + 1)]
	        numOfocc = occ.get(substr, 0)
	        occ[substr] = (numOfocc + 1)
	        if ((occ[substr] > 1) and (len(substr) > maxLen)):
	            maxLen = len(substr)
	return(maxLen)
