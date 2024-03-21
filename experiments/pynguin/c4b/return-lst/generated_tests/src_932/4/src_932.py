def func(*args):
	ret_values = []
	
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
	    if (x <= 4):
	        return 0
	    L = 0
	    R = (len(luckynums) - 1)
	    while (L < R):
	        M = ((L + R) // 2)
	        if (luckynums[M] < x):
	            L = (M + 1)
	        else:
	            R = M
	    return L
	(a, b) = tuple((int(i) for i in args[0].split()))
	sum = 0
	i = a
	while (i <= b):
	    nextv = next(i)
	    sum += (luckynums[nextv] * ((min(luckynums[nextv], b) - i) + 1))
	    i = (luckynums[nextv] + 1)
	ret_values.append(sum)

	return ret_values
