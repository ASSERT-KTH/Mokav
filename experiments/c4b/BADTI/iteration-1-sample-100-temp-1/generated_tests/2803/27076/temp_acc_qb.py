def patched_func(*args):
	global_list = []
	
	
	def chk(d):
	    s = (((d * (k - 1)) * k) // 2)
	    if ((n - s) > ((k - 1) * d)):
	        if (((n - s) % d) == 0):
	            return True
	    return False
	(n, k) = map(int, args[0].split())
	nod = (- 1)
	d = 1
	while ((d * d) <= n):
	    if chk(d):
	        nod = max(nod, d)
	    if chk((n // d)):
	        nod = max(nod, (n // d))
	    d += 1
	ans = ''
	if (nod > (- 1)):
	    for i in range(1, k):
	        ans += (str((nod * i)) + ' ')
	    global_list.append((ans + str((n - (((nod * (k - 1)) * k) // 2)))))
	else:
	    global_list.append((- 1))
	return global_list