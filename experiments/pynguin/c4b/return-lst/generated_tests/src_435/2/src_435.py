def func(*args):
	ret_values = []
	
	n = int(args[0].strip())
	l = 1
	k = 5
	lll = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	while (k <= n):
	    n = (n - k)
	    l += 1
	    k = (2 * k)
	l = (l - 1)
	k = (2 ** l)
	j = 0
	if (n == 0):
	    ret_values.append(lll[(- 1)])
	else:
	    for i in range(5):
	        if (n <= k):
	            ret_values.append(lll[j])
	            break
	        else:
	            n = (n - k)
	            j += 1

	return ret_values
