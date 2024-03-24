def func(*args):
	ret_values = []
	
	players = int(args[0])
	if (players == 2):
	    ret_values.append(1)
	elif (players == 3):
	    ret_values.append(2)
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
	    ret_values.append(answer)

	return ret_values
