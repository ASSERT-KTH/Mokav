def func(*args):
	
	n = int(args[0])
	l = list(map(int, args[1].split()))
	i = 0
	j = 0
	k = 0
	while (k < n):
	    k += l[j]
	    j += 1
	    i = j
	    if (j == 7):
	        j = 0
	return(i)
