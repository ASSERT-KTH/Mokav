def func(*args):
	ret_values = []
	
	from sys import stdin
	i = [int(x) for x in stdin.readline().rstrip().split()]
	n = i[0]
	r = sorted(i[1:])
	m = r[0]
	sec = r[1]
	third = r[2]
	step_count = (n // m)
	s = (n % m)
	res = None
	resList = set()
	if (s == 0):
	    ret_values.append(step_count)
	else:
	    while ((s != 0) and (s < n)):
	        s += m
	        step_count -= 1
	        for x in range((s // sec), (- 1), (- 1)):
	            if (not ((s - (x * sec)) % third)):
	                res = ((step_count + x) + ((s - (x * sec)) // third))
	                resList.add(res)
	                break
	    ret_values.append(max(resList))

	return ret_values
