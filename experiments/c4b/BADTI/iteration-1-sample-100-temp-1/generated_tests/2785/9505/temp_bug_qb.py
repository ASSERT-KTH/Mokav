def original_func(*args):
	global_list = []
	
	counter = 0
	bool = 1
	string = args[0]
	for i in range((len(string) - 1)):
	    if ((string[i] == 'V') and (string[(i + 1)] == 'K')):
	        counter += 1
	    elif ((string[i] == 'V') and (string[(i + 1)] == 'V') and (bool == 1)):
	        counter += 1
	        bool = 0
	    elif ((string[i] == 'K') and (string[(i + 1)] == 'K') and (bool == 1)):
	        counter += 1
	        bool = 0
	global_list.append(counter)
	return global_list