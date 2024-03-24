def func(*args):
	ret_values = []
	
	team = list(args[0])
	team = [int(i) for i in team]
	counter = 0
	index = 0
	flag = False
	for i in range(len(team)):
	    if ((counter >= 6) and (team[i] == team[index])):
	        flag = True
	        break
	    if (team[index] == team[i]):
	        counter += 1
	    else:
	        counter = 1
	        index = i
	if flag:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
