def func(*args):
	
	arr = [int(i) for i in args[0].split()]
	hsh = [0 for i in range(0, 101)]
	arr.sort()
	ans = 0
	for i in arr:
	    hsh[i] += 1
	    ans += i
	(i, temp, anst) = (100, ans, ans)
	while (i >= 1):
	    if (hsh[i] >= 3):
	        temp = (ans - (3 * i))
	        anst = min(anst, temp)
	    elif (hsh[i] >= 2):
	        temp = (ans - (2 * i))
	        anst = min(anst, temp)
	    i -= 1
	return(anst)
