def original_func(*args):
	global_list = []
	
	pstr = args[0].lower()
	plst = []
	a = '.'
	finstr = ''
	for i in range(0, len(pstr)):
	    plst.append(pstr[i])
	for i in range(0, len(plst)):
	    if (plst[i] in ['a', 'e', 'i', 'u', 'o']):
	        plst.pop(i)
	        plst.insert(i, finstr)
	    else:
	        pass
	i = 0
	while (i < len(plst)):
	    if (plst[i] == ''):
	        plst.pop(i)
	    else:
	        i += 1
	for i in plst:
	    finstr += a
	    finstr += i
	global_list.append(finstr)
	return global_list