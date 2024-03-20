def func(*args):
	
	(n, l, r) = map(int, args[0].split())
	binl = tuple(map(int, bin(n)[2:]))
	res = 0
	for i in range(len(binl)):
	    if (not binl[i]):
	        continue
	    cur = ((1 << i) + (((l >> (i + 1)) - 1) << (i + 1)))
	    dif = (1 << (i + 1))
	    while (cur <= r):
	        if (cur >= l):
	            res += 1
	        cur += dif
	return(res)
