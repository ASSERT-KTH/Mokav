def original_func(*args):
	global_list = []
	
	s = args[0]
	com = (- 1)
	cn = [(- 1)]
	for c in s:
	    while ((com != (- 1)) and (c != s[com])):
	        com = cn[com]
	    com += 1
	    cn.append(com)
	lenth = cn[(- 1)]
	if (cn.count(lenth) < 2):
	    lenth = cn[lenth]
	global_list.append((s[:lenth] if (lenth > 0) else 'Just a legend'))
	return global_list