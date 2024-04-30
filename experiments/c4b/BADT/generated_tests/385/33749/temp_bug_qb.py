def original_func(*args):
	global_list = []
	
	(h1, h2) = tuple(map(int, args[0].split()))
	(a, b) = tuple(map(int, args[1].split()))
	'\n\na =2 #скорость вверх\n\nb =1 #скорость сползания\n\nh1 =1 #старт червя\n\nh2 =300 #высота яблока\n\nr = a #переменная текущего положения\n\n'
	day = 0
	r = ((a * 8) + h1)
	if ((a <= b) and (((a * 8) + h1) <= h2)):
	    day = (- 1)
	elif ((a <= b) and (r < h2)):
	    day = (- 1)
	else:
	    while (r < h2):
	        r = (r - (b * 12))
	        r = (r + (a * 12))
	        day = (day + 1)
	global_list.append(day)
	return global_list