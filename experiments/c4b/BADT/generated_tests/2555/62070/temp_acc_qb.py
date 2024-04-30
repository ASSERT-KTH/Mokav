def patched_func(*args):
	global_list = []
	
	gamers = args[0]
	pol = 1
	i = 1
	for j in range(1, len(gamers)):
	    if (gamers[j] == gamers[(j - 1)]):
	        pol += 1
	    elif ((pol < 7) and (gamers[j] != gamers[(j - 1)])):
	        pol = 1
	if (pol >= 7):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list