def original_func(*args):
	global_list = []
	
	(hobs, pillows, frodo) = args[0].split()
	(hobs, pillows, frodo) = (int(hobs), int(pillows), int(frodo))
	turn = 0
	left = frodo
	right = frodo
	pilCount = 1
	pillows -= hobs
	while True:
	    if ((left <= 1) and (right > hobs)):
	        pilCount += (pillows // hobs)
	        break
	    elif ((left <= 1) or (right > hobs)):
	        pillows -= (turn + 1)
	    else:
	        pillows -= ((turn * 2) + 1)
	    if (pillows < 0):
	        break
	    left -= 1
	    right += 1
	    pilCount += 1
	    turn += 1
	global_list.append(pilCount)
	return global_list