def patched_func(*args):
	global_list = []
	
	(s, x) = args[0].split()
	(s, x) = (int(s), int(x))
	ones_in_x = 0
	for let in reversed('{0:b}'.format(x)):
	    if (let == '1'):
	        ones_in_x += 1
	zbytkove = (s - x)
	if (((zbytkove % 2) == 1) or (x > s)):
	    global_list.append(0)
	elif (s == x):
	    global_list.append(((2 ** ones_in_x) - 2))
	else:
	    for (zb, let) in zip(reversed('{0:b}'.format((zbytkove // 2))), reversed('{0:b}'.format(x))):
	        if ((zb == '1') and (zb == let)):
	            global_list.append(0)
	            break
	    else:
	        global_list.append((2 ** ones_in_x))
	return global_list