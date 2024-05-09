def original_func(*args):
	global_list = []
	
	(N, K) = [n for n in args[0].split()]
	K = int(K)
	i = 0
	dels = 0
	for d in reversed(N):
	    if (i < K):
	        if (d != '0'):
	            dels += 1
	            i -= 1
	    else:
	        break
	    i += 1
	if (K >= len(N)):
	    global_list.append((len(N) - 1))
	else:
	    global_list.append(dels)
	return global_list