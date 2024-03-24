def func(*args):
	
	(n, k) = map(int, args[0].split())
	a = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
	dienos = a[n]
	j = 0
	i = (k - 1)
	for t in range(a[n]):
	    if (i == 7):
	        j += 1
	        i = 0
	    if ((t == (a[n] - 1)) and (i != 7)):
	        j += 1
	    i += 1
	return(j)
