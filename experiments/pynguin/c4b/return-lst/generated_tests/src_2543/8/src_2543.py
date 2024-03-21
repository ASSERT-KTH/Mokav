def func(*args):
	ret_values = []
	
	import sys
	(n, k) = map(int, sys.stdin.readline().split())
	if (((k == 1) and (n != 1)) or (k > n)):
	    ret_values.append((- 1))
	elif (n == 1):
	    ret_values.append('a')
	else:
	    tmp = ((n - k) + 2)
	    s = ('ab' * (tmp // 2))
	    if ((tmp % 2) == 1):
	        s += 'a'
	    for i in range(2, k):
	        s += chr((ord('a') + i))
	    ret_values.append(s)

	return ret_values
