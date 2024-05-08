def original_func(*args):
	global_list = []
	
	(a, b, c, d) = map(int, args[0].split())
	if (((a + b) > c) and ((a + c) > b) and ((b + c) > a)):
	    global_list.append('TRIANGLE 1')
	elif (((a + b) > d) and ((a + d) > b) and ((b + d) > a)):
	    global_list.append('TRIANGLE 2')
	elif (((a + c) > d) and ((a + d) > c) and ((c + d) > a)):
	    global_list.append('TRIANGLE 3')
	elif (((b + c) > d) and ((b + d) > c) and ((c + d) > b)):
	    global_list.append('TRIANGLE 4')
	elif (((a + b) == c) or ((a + c) == b) or ((b + c) == a)):
	    global_list.append('SEGMENT 1')
	elif (((a + b) == d) or ((a + d) == b) or ((b + d) == a)):
	    global_list.append('SEGMENT 2')
	elif (((a + c) == d) or ((a + d) == c) or ((c + d) == a)):
	    global_list.append('SEGMENT 3')
	elif (((b + c) == d) or ((b + d) == c) or ((c + d) == b)):
	    global_list.append('SEGMENT 4')
	else:
	    global_list.append('IMPOSSIBLE')
	return global_list