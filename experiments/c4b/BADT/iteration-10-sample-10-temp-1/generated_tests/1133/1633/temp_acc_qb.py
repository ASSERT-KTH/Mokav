def patched_func(*args):
	global_list = []
	
	s = args[0]
	a = len(s)
	numbers = {}
	for x in range(a):
	    for y in range((x + 1), (a + 1)):
	        t = s[x:y]
	        for z in t:
	            p = int(z)
	            if ((p != 4) and (p != 7)):
	                break
	        else:
	            p = int(t)
	            if (not (p in numbers)):
	                numbers[p] = 0
	            numbers[p] += 1
	if (numbers == {}):
	    global_list.append((- 1))
	else:
	    global_list.append(min(filter((lambda x: (numbers[x] == max(numbers.values()))), numbers.keys())))
	return global_list