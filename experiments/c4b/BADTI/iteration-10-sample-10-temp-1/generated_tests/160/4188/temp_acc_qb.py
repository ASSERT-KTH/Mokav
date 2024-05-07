def patched_func(*args):
	global_list = []
	
	(a, b) = [int(x) for x in args[0].split()]
	answer = 0
	if ((a == 1) and (b == 1)):
	    global_list.append(0)
	else:
	    power = 2
	    while (power < 61):
	        fullones = ((2 ** power) - 1)
	        tosubtract = 1
	        pos = 1
	        while (pos < power):
	            test = (fullones - tosubtract)
	            if ((test >= a) and (test <= b)):
	                answer += 1
	            tosubtract *= 2
	            pos += 1
	        power += 1
	    global_list.append(answer)
	return global_list