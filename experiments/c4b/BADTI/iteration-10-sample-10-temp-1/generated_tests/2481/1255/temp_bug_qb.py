def original_func(*args):
	global_list = []
	
	n = int(args[0])
	k = 1
	max = 0
	while True:
	    max = (max + ((2 ** k) * 5))
	    min = (max - ((2 ** k) * 5))
	    if (min <= n <= max):
	        break
	    k += 1
	if (((n - min) % (2 ** k)) == 0):
	    who = ((n - min) // (2 ** k))
	elif (((n - min) % (2 ** k)) != 0):
	    who = (((n - min) // (2 ** k)) + 1)
	if (who == 1):
	    global_list.append('Sheldon')
	elif (who == 2):
	    global_list.append('Leonard')
	elif (who == 3):
	    global_list.append('Penny')
	elif (who == 4):
	    global_list.append('Rajesh')
	elif (who == 5):
	    global_list.append('Howard')
	return global_list