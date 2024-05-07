def original_func(*args):
	global_list = []
	
	w = args[0].lower()
	wf = ''
	for itch in range(0, len(w)):
	    if ((w[itch] == 'a') or (w[itch] == 'e') or (w[itch] == 'i') or (w[itch] == 'o') or (w[itch] == 'u')):
	        continue
	    else:
	        wf += ('.' + w[itch])
	global_list.append(wf)
	return global_list