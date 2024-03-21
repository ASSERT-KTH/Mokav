def func(*args):
	ret_values = []
	
	
	def typecontest(s, v1, v2, t1, t2):
	    Firsttakes = ((v1 * s) + (2 * t1))
	    Secondtakes = ((v2 * s) + (2 * t2))
	    if (Firsttakes < Secondtakes):
	        ret_values.append('First')
	    elif (Firsttakes > Secondtakes):
	        ret_values.append('Second')
	    else:
	        ret_values.append('Friendship')
	    return
	(s, v1, v2, t1, t2) = list(map(int, args[0].strip().split()))
	typecontest(s, v1, v2, t1, t2)

	return ret_values
