def patched_func(*args):
	global_list = []
	
	(x, y, z, k) = [int(x) for x in args[0].split()]
	dim = sorted([(x - 1), (y - 1), (z - 1)])
	answer = [0, 0, 0]
	for i in range(len(dim)):
	    dimi = dim[i]
	    if ((dimi * (3 - i)) <= k):
	        k = (k - (dimi * (3 - i)))
	        for j in range(i, 3):
	            answer[j] += dimi
	        for j in range(3):
	            dim[j] -= dimi
	    else:
	        for j in range(i, 3):
	            answer[j] += (k // (3 - i))
	        for j in range(i, ((k % (3 - i)) + i)):
	            answer[j] += 1
	        break
	true_ans = 1
	for i in answer:
	    true_ans = (true_ans * (i + 1))
	global_list.append(true_ans)
	return global_list