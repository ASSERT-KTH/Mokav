def original_func(*args):
	global_list = []
	
	luckynums = []
	for digits in range(1, 10):
	    for mask in range((1 << digits)):
	        num = ''
	        for i in range(digits):
	            if ((mask & (1 << i)) == 0):
	                num = ('4' + num)
	            else:
	                num = ('7' + num)
	        luckynums.append(int(num))
	luckynums.append(4444444444)
	
	def next(x):
	    L = 0
	    R = (len(luckynums) - 1)
	    while (L < R):
	        M = ((L + R) // 2)
	        if (luckynums[M] <= x):
	            L = (M + 1)
	        else:
	            R = M
	    return L
	(a, b) = tuple((int(i) for i in args[0].split()))
	sum = 0
	prev = (- 1)
	i = a
	if (((i - 2) > 0) and (next((i - 2)) != (i - 1))):
	    i = (a - 1)
	    prev = (- 2)
	while (i < b):
	    nextv = next(i)
	    if (prev != (- 1)):
	        sum += (luckynums[nextv] * (min(luckynums[nextv], b) - i))
	    else:
	        sum += (luckynums[nextv] * ((min(luckynums[nextv], b) - i) + 1))
	    prev = nextv
	    i = luckynums[nextv]
	global_list.append(sum)
	return global_list