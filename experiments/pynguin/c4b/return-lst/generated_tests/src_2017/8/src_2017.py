def func(*args):
	ret_values = []
	
	venusian_fingers = [int(n) for n in args[0].split()]
	marsian_fingers = [int(n) for n in args[1].split()]
	yes = False
	for i in range(0, 2):
	    if ((marsian_fingers[(1 - i)] <= ((venusian_fingers[i] + 1) * 2)) and (marsian_fingers[(i - 1)] >= (venusian_fingers[i] - 1))):
	        yes = True
	        break
	if yes:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
