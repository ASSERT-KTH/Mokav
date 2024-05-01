def patched_func(*args):
	global_list = []
	
	(n, t) = map(int, args[0].split())
	ppl = list(args[1])
	for i in range(t):
	    p = 0
	    for z in range((len(ppl) - 1)):
	        if p:
	            p = 0
	            continue
	        if ((ppl[z] == 'B') and (ppl[(z + 1)] == 'G')):
	            (ppl[z], ppl[(z + 1)]) = (ppl[(z + 1)], ppl[z])
	            p = 1
	ppl = ''.join(ppl)
	global_list.append(ppl)
	return global_list