def original_func(*args):
	global_list = []
	
	x = int(args[0])
	if ((x >= (- 128)) and (x <= 127)):
	    global_list.append('byte')
	elif ((x >= (- 32768)) and (x <= 32767)):
	    global_list.append('short')
	elif ((x >= (- 214783648)) and (x <= 214783647)):
	    global_list.append('int')
	elif ((x >= (- 9223372036854775808)) and (x <= 9223372036854775807)):
	    global_list.append('long')
	else:
	    global_list.append('BigInteger')
	return global_list