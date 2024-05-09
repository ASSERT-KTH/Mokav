def original_func(*args):
	global_list = []
	
	string = args[0]
	numbers = string.split()
	for x in range(5):
	    numbers[x] = int(numbers[x])
	a = numbers[0]
	b = numbers[1]
	c = numbers[2]
	d = numbers[3]
	e = numbers[4]
	p = max([a, c])
	q = min([b, d])
	r = ((q - p) + 1)
	if (p <= e <= q):
	    r -= 1
	if (r < 0):
	    (r == 0)
	global_list.append(r)
	return global_list