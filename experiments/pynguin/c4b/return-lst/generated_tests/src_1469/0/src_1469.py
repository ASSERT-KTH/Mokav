def func(*args):
	ret_values = []
	
	ll = []
	for x in range(3, 1001):
	    l = list(str(x))
	    if (len(l) == (l.count('4') + l.count('7'))):
	        ll.append(x)
	tmp = int(args[0])
	t = 0
	for i in ll:
	    if ((tmp % i) == 0):
	        ret_values.append('YES')
	        t = 1
	        break
	if (t == 0):
	    ret_values.append('NO')

	return ret_values
