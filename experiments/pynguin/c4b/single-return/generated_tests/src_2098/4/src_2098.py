def func(*args):
	
	(c, v, vm, a, l) = list(map(int, args[0].split()))
	pos = v
	time = 1
	add = v
	while (pos < c):
	    add = min(vm, (add + a))
	    pos += (add - l)
	    time += 1
	return(time)
