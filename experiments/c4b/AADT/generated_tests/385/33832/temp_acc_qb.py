def patched_func(*args):
	global_list = []
	
	(h1, h2) = map(int, args[0].split())
	(a, b) = map(int, args[1].split())
	day = 0
	while (h1 < h2):
	    if (day == 0):
	        h1 += (a * 8)
	        if ((h1 < h2) and (b >= a)):
	            global_list.append((- 1))
	            break
	        elif (h1 < h2):
	            h1 -= (b * 12)
	            day += 1
	        while (h1 < h2):
	            h1 += (a * 12)
	            if (h1 < h2):
	                h1 -= (b * 12)
	                day += 1
	        global_list.append(day)
	return global_list