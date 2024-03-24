def func(*args):
	
	from itertools import combinations
	nl = list(map(int, args[0].split()))
	ol = args[1].split()
	ans = 10000000000000
	for x in combinations(nl, 2):
	    (a, b) = x
	    tl = nl[:]
	    tl.remove(a)
	    tl.remove(b)
	    if (ol[0] == '+'):
	        tl.append((a + b))
	    else:
	        tl.append((a * b))
	    for y in combinations(tl, 2):
	        (i, j) = y
	        sl = tl[:]
	        sl.remove(i)
	        sl.remove(j)
	        if (ol[1] == '+'):
	            sl.append((i + j))
	        else:
	            sl.append((i * j))
	        if (ol[2] == '+'):
	            mm = (sl[0] + sl[1])
	        else:
	            mm = (sl[0] * sl[1])
	        if (ans > mm):
	            ans = mm
	return(ans)
