def func(*args):
	ret_values = []
	
	from sys import stdin
	
	def quick(n):
	    if (len(n) == 0):
	        return n
	    piv = n[(len(n) // 2)]
	    (mi, me, ma) = ([], [], [])
	    for i in range(len(n)):
	        if (n[i] < piv):
	            mi.append(n[i])
	        elif (n[i] > piv):
	            ma.append(n[i])
	        elif (n[i] == piv):
	            me.append(n[i])
	    return ((quick(ma) + me) + quick(mi))
	m = int(stdin.readline().strip())
	n = list(map(int, stdin.readline().strip().split()))
	l = quick(n)
	p = 1
	cont = l[0]
	for i in range((len(l) - 1)):
	    if (cont < m):
	        cont += l[(i + 1)]
	        p += 1
	if (m == 0):
	    ret_values.append(0)
	elif (cont < m):
	    ret_values.append((- 1))
	else:
	    ret_values.append(p)

	return ret_values
