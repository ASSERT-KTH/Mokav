def patched_func(*args):
	global_list = []
	
	s = [int(i) for i in args[0].split()]
	i = 1
	x = y = z = 0
	while (i < 3):
	    if (s[i] < s[(i + 1)]):
	        (s[i], s[(i + 1)]) = (s[(i + 1)], s[i])
	        i = 0
	    i += 1
	if (s[0] % s[3]):
	    k = round(((s[0] - (s[0] % s[3])) / s[3]))
	    h = (s[0] % s[3])
	    while (k > 0):
	        k -= 1
	        h += s[3]
	        if ((h % s[2]) == 0):
	            k += round((h / s[2]))
	            break
	    x = k
	    k = round(((s[0] - (s[0] % s[3])) / s[3]))
	    h = (s[0] % s[3])
	    while (k > 0):
	        k -= 1
	        h += s[3]
	        if ((h % s[1]) == 0):
	            k += round((h / s[1]))
	            break
	    y = k
	    if (x > y):
	        y = x
	    k = round(((s[0] - (s[0] % s[3])) / s[3]))
	    h = (s[0] % s[3])
	    while (k > 0):
	        k -= 1
	        h += s[3]
	        if ((h % s[2]) == 0):
	            k += round((h / s[2]))
	            break
	        elif ((h % s[1]) == 0):
	            k += round((h / s[1]))
	            break
	        elif ((h % (s[1] + s[2])) == 0):
	            k += (2 * round((h / (s[1] + s[2]))))
	            break
	    z = k
	    if (y > z):
	        k = y
	    if k:
	        global_list.append(k)
	    elif (s[0] % s[2]):
	        k = round(((s[0] - (s[0] % s[2])) / s[2]))
	        h = (s[0] % s[2])
	        while (k > 0):
	            k -= 1
	            h += s[2]
	            if ((h % s[2]) == 0):
	                k += round((h / s[2]))
	                break
	        if k:
	            global_list.append(k)
	        else:
	            global_list.append(round((s[0] / s[1])))
	    else:
	        global_list.append(round((s[0] / s[2])))
	else:
	    global_list.append(round((s[0] / s[3])))
	return global_list