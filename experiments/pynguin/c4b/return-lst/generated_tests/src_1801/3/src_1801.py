def func(*args):
	ret_values = []
	
	V = [args[0].count('B') for _ in range(8)]
	cnt = 0
	for i in V:
	    if (i == 8):
	        cnt += 1
	if (min(V) != 8):
	    cnt += min(V)
	ret_values.append(cnt)

	return ret_values
