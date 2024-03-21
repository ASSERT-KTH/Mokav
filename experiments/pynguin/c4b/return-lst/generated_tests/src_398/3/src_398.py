def func(*args):
	ret_values = []
	
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
	    ret_values.append((- 1))
	else:
	    ret_values.append(min(filter((lambda x: (numbers[x] == max(numbers.values()))), numbers.keys())))

	return ret_values
