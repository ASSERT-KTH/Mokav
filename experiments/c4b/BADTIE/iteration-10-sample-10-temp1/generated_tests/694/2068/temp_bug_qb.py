def original_func(*args):
	global_list = []
	
	n = args[0]
	if (((n[0] == 'a') and (n[1] != 1) and (n[1] != 8)) or ((n[0] == 'h') and (n[1] != 1) and (n[1] != 8)) or ((n[1] == '1') and (n[0] != 'a') and (n[0] != 'h')) or ((n[1] == '8') and (n[0] != 'a') and (n[0] != 'h'))):
	    global_list.append(5)
	else:
	    global_list.append(8)
	return global_list