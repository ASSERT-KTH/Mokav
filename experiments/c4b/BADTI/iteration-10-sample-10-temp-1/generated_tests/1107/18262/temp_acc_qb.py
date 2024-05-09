def patched_func(*args):
	global_list = []
	
	
	def gcd(a, b):
	    c = max(a, b)
	    while (c > 0):
	        if (((a % c) == 0) and ((b % c) == 0)):
	            return c
	        elif (c > min(a, b)):
	            c = min(a, b)
	            continue
	        else:
	            c -= 1
	            continue
	inp = [int(i) for i in args[0].split()]
	n = inp[2]
	win = 0
	lose = 0
	turn = True
	while (n > 0):
	    if (turn == True):
	        n = (n - gcd(inp[0], n))
	        win += 1
	        turn = False
	        continue
	    elif (turn == False):
	        n = (n - gcd(inp[1], n))
	        lose += 1
	        turn = True
	        continue
	if (win > lose):
	    global_list.append(0)
	else:
	    global_list.append(1)
	return global_list