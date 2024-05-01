def patched_func(*args):
	global_list = []
	
	'satr=[int(x) for x in input().split(" ")]'
	satr = args[0]
	S = 0
	koor = 1
	for i in satr:
	    if ((i == 'A') or (i == 'E') or (i == 'I') or (i == 'U') or (i == 'O') or (i == 'Y')):
	        if (koor > S):
	            S = koor
	        koor = 0
	    koor += 1
	if (koor > S):
	    S = koor
	global_list.append(str(S))
	return global_list