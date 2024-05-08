def original_func(*args):
	global_list = []
	
	(n, t) = args[0].split()
	seq = list(args[1])
	for i in range(int(t)):
	    newSeq = []
	    is_change = False
	    for j in range((int(n) - 1)):
	        if is_change:
	            is_change = False
	            continue
	        if ((seq[j] == 'B') and (seq[(j + 1)] == 'G')):
	            newSeq.append('G')
	            newSeq.append('B')
	            is_change = True
	        else:
	            newSeq.append(seq[j])
	        if (j == (int(n) - 2)):
	            if (len(newSeq) != len(seq)):
	                newSeq.append(seq[(j + 1)])
	    seq = newSeq
	global_list.append(''.join(seq))
	return global_list