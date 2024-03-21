def func(*args):
	ret_values = []
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	speed = v0
	pages = v0
	days = 1
	while (pages < c):
	    if ((speed + a) <= v1):
	        speed += a
	    else:
	        speed = v1
	    pages = ((pages + speed) - l)
	    days += 1
	ret_values.append(days)

	return ret_values
