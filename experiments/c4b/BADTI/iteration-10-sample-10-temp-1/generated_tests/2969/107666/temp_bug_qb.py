def original_func(*args):
	global_list = []
	
	
	def typecontest(s, v1, v2, t1, t2):
	    Firsttakes = ((v1 * s) + (2 * t1))
	    global_list.append(Firsttakes)
	    Secondtakes = ((v2 * s) + (2 * t2))
	    global_list.append(Secondtakes)
	    if (Firsttakes < Secondtakes):
	        global_list.append('First')
	    elif (Firsttakes > Secondtakes):
	        global_list.append('Second')
	    else:
	        global_list.append('Friendship')
	    return
	(s, v1, v2, t1, t2) = list(map(int, args[0].strip().split()))
	typecontest(s, v1, v2, t1, t2)
	return global_list