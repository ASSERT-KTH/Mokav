def original_func(*args):
	global_list = []
	
	friends = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = int(args[0])
	a = (n % 5)
	if (n > 5):
	    if (a == 0):
	        global_list.append('Howard')
	    elif (a == 4):
	        global_list.append('Rajesh')
	    elif (a == 3):
	        global_list.append('Penny')
	    elif (a == 2):
	        global_list.append('Leonard')
	    elif (a == 1):
	        global_list.append('Sheldon')
	elif (n <= 5):
	    if (n == 5):
	        global_list.append('Howard')
	    elif (n == 4):
	        global_list.append('Rajesh')
	    elif (n == 3):
	        global_list.append('Penny')
	    elif (n == 2):
	        global_list.append('Leonard')
	    elif (n == 1):
	        global_list.append('Sheldon')
	return global_list