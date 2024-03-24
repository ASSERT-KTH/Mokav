def func(*args):
	
	
	def task():
	    (a, b, c, d) = args[0].split()
	    (a, b, c, d) = [int(a), int(b), int(c), int(d)]
	    if ((((a + b) > c) and ((a + c) > b) and ((c + b) > a)) or (((d + a) > b) and ((d + b) > a) and ((a + b) > d)) or (((a + c) > d) and ((c + d) > a) and ((d + a) > c)) or (((b + c) > d) and ((b + d) > c) and ((d + c) > b))):
	        return 'TRIANGLE'
	    elif (((a + b) == c) or ((a + d) == c) or ((d + b) == c) or ((a + c) == d) or ((a + b) == d) or ((c + b) == d) or ((c + b) == a) or ((c + d) == a) or ((d + b) == a) or ((a + c) == b) or ((a + d) == b) or ((c + d) == b)):
	        return 'SEGMENT'
	    else:
	        return 'IMPOSSIBLE'
	return(task())
