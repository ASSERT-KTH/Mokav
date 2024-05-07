def original_func(*args):
	global_list = []
	
	n = int(args[0])
	kartu = 10
	powarray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
	for i in range(len(powarray)):
	    if ((kartu + powarray[i]) == n):
	        global_list.append('4')
	if ((kartu + 10) == n):
	    global_list.append('15')
	elif ((n == 10) or (n > 21)):
	    global_list.append('0')
	return global_list