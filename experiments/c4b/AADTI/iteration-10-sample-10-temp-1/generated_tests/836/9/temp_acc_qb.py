def patched_func(*args):
	global_list = []
	
	players = int(args[0])
	if (players == 2):
	    global_list.append(1)
	elif (players == 3):
	    global_list.append(2)
	else:
	    fib = 3
	    fist = 2
	    sec = 3
	    answer = 2
	    while (fib < players):
	        answer += 1
	        fib = (fist + sec)
	        fist = sec
	        sec = fib
	    if (fib > players):
	        answer -= 1
	    global_list.append(answer)
	return global_list