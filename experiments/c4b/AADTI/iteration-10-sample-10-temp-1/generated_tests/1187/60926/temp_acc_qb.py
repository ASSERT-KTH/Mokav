def patched_func(*args):
	global_list = []
	
	lisa = args[0]
	if (lisa == lisa.upper()):
	    global_list.append(lisa.lower())
	elif ((lisa == (lisa[0].lower() + lisa[1:].upper())) and (len(lisa) > 1)):
	    global_list.append((lisa[0].upper() + lisa[1:].lower()))
	elif (len(lisa) == 1):
	    global_list.append(lisa.upper())
	else:
	    global_list.append(lisa)
	return global_list