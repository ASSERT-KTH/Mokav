def func(*args):
	ret_values = []
	
	gamers = args[0]
	pol = 1
	i = 1
	for j in range(1, len(gamers)):
	    if (gamers[j] == gamers[(j - 1)]):
	        pol += 1
	    elif ((pol < 7) and (gamers[j] != gamers[(j - 1)])):
	        pol = 1
	if (pol >= 7):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
