def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	if (a >= 13):
	    if (a == 13):
	        global_list.append(8092)
	    if (a == 14):
	        global_list.append(16184)
	    if (a == 15):
	        global_list.append(32368)
	    if (a == 16):
	        global_list.append(64736)
	    if (a == 17):
	        global_list.append(129472)
	    if (a == 18):
	        global_list.append(258944)
	    if (a == 19):
	        global_list.append(517888)
	    if (a == 20):
	        global_list.append(1035776)
	    if (a == 21):
	        global_list.append(2071552)
	    if (a == 22):
	        global_list.append(4143104)
	    if (a == 23):
	        global_list.append(8286208)
	    if (a == 24):
	        global_list.append(16572416)
	    if (a == 25):
	        global_list.append(33144832)
	    if (a == 26):
	        global_list.append(66289664)
	    if (a == 27):
	        global_list.append(132579328)
	    if (a == 28):
	        global_list.append(265158656)
	    if (a == 29):
	        global_list.append(530317312)
	    if (a == 30):
	        global_list.append(1060634624)
	    if (a == 31):
	        global_list.append(2121269248)
	    if (a == 32):
	        global_list.append(4242538496)
	    if (a == 33):
	        global_list.append(8485076992)
	    if (a == 34):
	        global_list.append(16970153984)
	    if (a == 35):
	        global_list.append(33940307968)
	else:
	    global_list.append(pow(2, a))
	return global_list