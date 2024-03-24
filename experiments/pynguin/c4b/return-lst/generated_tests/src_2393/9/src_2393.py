def func(*args):
	ret_values = []
	
	sticks = list(map(int, args[0].split()))
	sticks.sort()
	sticks.reverse()
	if ((sticks[0] < (sticks[1] + sticks[2])) or (sticks[1] < (sticks[2] + sticks[3]))):
	    ret_values.append('TRIANGLE')
	elif ((sticks[0] == (sticks[1] + sticks[2])) or (sticks[1] == (sticks[2] + sticks[3]))):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
