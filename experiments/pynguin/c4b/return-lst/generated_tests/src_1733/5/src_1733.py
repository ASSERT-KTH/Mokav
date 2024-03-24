def func(*args):
	ret_values = []
	
	count = int(args[0])
	std = ['NULL', 'Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	fn = ''
	if (count <= 5):
	    ret_values.append(std[count])
	else:
	
	    def findblock(cnt):
	        b = 0
	        ob = 0
	        nb = 0
	        while (nb < cnt):
	            ob = nb
	            nb += (5 * (2 ** b))
	            b += 1
	        return [b, ob, nb, count]
	    kf = findblock(count)
	    tm = kf[1]
	    shg = kf[0]
	    db = 0
	    while (tm < count):
	        tm += (2 ** (shg - 1))
	        db += 1
	    ret_values.append(std[db])

	return ret_values
