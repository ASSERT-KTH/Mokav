def original_func(*args):
	global_list = []
	
	players = int(args[0])
	games = 0
	while True:
	    lastpcount = players
	    players = (players // 2)
	    games += 1
	    if (((2 * players) == lastpcount) and (players == 1)):
	        break
	    elif ((2 * players) != lastpcount):
	        players += 1
	global_list.append(games)
	return global_list