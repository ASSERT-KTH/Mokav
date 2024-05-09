def original_func(*args):
	global_list = []
	
	sticks = list(map(int, args[0].split()))
	sticks.sort()
	sticks.reverse()
	global_list.append(sticks)
	if ((sticks[0] < (sticks[1] + sticks[2])) or (sticks[1] < (sticks[2] + sticks[3]))):
	    global_list.append('TRIANGLE')
	elif ((sticks[0] == (sticks[1] + sticks[2])) or (sticks[1] == (sticks[2] + sticks[3]))):
	    global_list.append('SEGMENT')
	else:
	    global_list.append('IMPOSSIBLE')
	return global_list