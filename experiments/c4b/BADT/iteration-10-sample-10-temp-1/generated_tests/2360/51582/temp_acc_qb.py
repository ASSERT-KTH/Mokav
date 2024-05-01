def patched_func(*args):
	global_list = []
	
	venusian_fingers = [int(n) for n in args[0].split()]
	marsian_fingers = [int(n) for n in args[1].split()]
	yes = False
	for i in range(0, 2):
	    if ((marsian_fingers[(1 - i)] <= ((venusian_fingers[i] + 1) * 2)) and (marsian_fingers[(i - 1)] >= (venusian_fingers[i] - 1))):
	        yes = True
	        break
	if yes:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list