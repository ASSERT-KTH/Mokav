def func(*args):
	ret_values = []
	
	(n, k) = args[0].split()
	n = int(n)
	k = int(k)
	a1 = args[1]
	a = []
	count = 0
	result = 100
	q = ''
	if ((1 <= n <= 50) and (1 <= k <= 50)):
	    for i in a1:
	        if ((i == 'B') or (i == 'G')):
	            count = (count + 1)
	    if (count == n):
	        for p in a1:
	            a.append(p)
	        for i in range(0, k):
	            for j in range(0, (len(a) - 1)):
	                if ((a[j] == 'B') and (a[(j + 1)] == 'G') and (j != (result + 1))):
	                    c = a[j]
	                    a[j] = a[(j + 1)]
	                    a[(j + 1)] = c
	                    result = j
	            result = 100
	        for n in a:
	            q = (q + n)
	        ret_values.append(q)

	return ret_values
