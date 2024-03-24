def func(*args):
	
	(n, t) = args[0].split()
	seq = list(args[1])
	for i in range(int(t)):
	    switchs = []
	    for j in range((int(n) - 1)):
	        if ((seq[j] == 'B') and (seq[(j + 1)] == 'G')):
	            switchs.append(j)
	    for switch in switchs:
	        (seq[switch], seq[(switch + 1)]) = (seq[(switch + 1)], seq[switch])
	return(''.join(seq))
