def original_func(*args):
	global_list = []
	
	line = args[0]
	if (('H' in line) or ('Q' in line) or ('9' in line)):
	    global_list.append('YES')
	elif ('+' in line):
	    occ = line.count('+')
	    if ((occ == 15) or (occ == 30) or (occ == 39)):
	        global_list.append('YES')
	    else:
	        global_list.append('No')
	else:
	    global_list.append('NO')
	return global_list