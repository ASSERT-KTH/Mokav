def func(*args):
	ret_values = []
	
	(n, k) = [int(x) for x in args[0].split()]
	cnt = 0
	p = 2
	V = []
	while (p <= n):
	    if ((n % p) == 0):
	        n //= p
	        cnt += 1
	        V.append(p)
	        if (cnt == k):
	            break
	    else:
	        p += 1
	if ((cnt == k) and (n > 1)):
	    V[(cnt - 1)] *= n
	if (cnt < k):
	    ret_values.append((- 1))
	else:
	    for i in range(0, cnt):
	        ret_values.append(V[i], end=' ')

	return ret_values
