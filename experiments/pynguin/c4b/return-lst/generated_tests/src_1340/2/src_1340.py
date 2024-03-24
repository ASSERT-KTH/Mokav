def func(*args):
	ret_values = []
	
	a = int(args[0])
	if (a >= 13):
	    if (a == 13):
	        ret_values.append(8092)
	    if (a == 14):
	        ret_values.append(16184)
	    if (a == 15):
	        ret_values.append(32368)
	    if (a == 16):
	        ret_values.append(64736)
	    if (a == 17):
	        ret_values.append(129472)
	    if (a == 18):
	        ret_values.append(258944)
	    if (a == 19):
	        ret_values.append(517888)
	    if (a == 20):
	        ret_values.append(1035776)
	    if (a == 21):
	        ret_values.append(2071552)
	    if (a == 22):
	        ret_values.append(4143104)
	    if (a == 23):
	        ret_values.append(8286208)
	    if (a == 24):
	        ret_values.append(16572416)
	    if (a == 25):
	        ret_values.append(33144832)
	    if (a == 26):
	        ret_values.append(66289664)
	    if (a == 27):
	        ret_values.append(132579328)
	    if (a == 28):
	        ret_values.append(265158656)
	    if (a == 29):
	        ret_values.append(530317312)
	    if (a == 30):
	        ret_values.append(1060634624)
	    if (a == 31):
	        ret_values.append(2121269248)
	    if (a == 32):
	        ret_values.append(4242538496)
	    if (a == 33):
	        ret_values.append(8485076992)
	    if (a == 34):
	        ret_values.append(16970153984)
	    if (a == 35):
	        ret_values.append(33940307968)
	else:
	    ret_values.append(pow(2, a))

	return ret_values
