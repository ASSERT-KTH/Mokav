def original_func(*args):
	global_list = []
	
	(x, t, a, b, da, db) = map(int, args[0].split())
	ans = 0
	if (x == 0):
	    t = 0
	    ans = 1
	for i in range(t):
	    for j in range(t):
	        if ((((a - (i * da)) + b) - (j * db)) == x):
	            ans = 1
	            break
	    if (ans == 1):
	        break
	global_list.append(['NO', 'YES'][ans])
	return global_list