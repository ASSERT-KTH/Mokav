def original_func(*args):
	global_list = []
	
	players = args[0]
	control = 1
	ok = 'NO'
	for i in range((len(players) - 1)):
	    if (players[i] == players[(i + 1)]):
	        control += 1
	    else:
	        if (control > 6):
	            ok = 'YES'
	            break
	        control = 1
	global_list.append(ok)
	return global_list