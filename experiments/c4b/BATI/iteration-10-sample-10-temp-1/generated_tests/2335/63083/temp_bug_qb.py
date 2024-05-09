def original_func(*args):
	global_list = []
	
	s = args[0]
	h_index = s.find('h')
	o_index = s.rfind('o')
	if ((h_index == (- 1)) or (o_index == (- 1)) or (h_index >= o_index)):
	    global_list.append('NO')
	else:
	    s = s[h_index:(o_index + 1)]
	    e_index = s.find('e')
	    l_index = s.find('ll')
	    o_index = s.find('o')
	    if ((e_index == (- 1)) or (l_index == (- 1))):
	        global_list.append('NO')
	    else:
	        h = s[:e_index]
	        e = s[e_index:l_index]
	        ll = s[l_index:o_index]
	        o = s[o_index:]
	        if (all(((c in 'h') for c in h)) and all(((c in 'e') for c in e)) and all(((c in 'l') for c in ll)) and (ll.count('l') > 1) and all(((c in 'o') for c in o))):
	            global_list.append('YES')
	        else:
	            global_list.append('NO')
	return global_list