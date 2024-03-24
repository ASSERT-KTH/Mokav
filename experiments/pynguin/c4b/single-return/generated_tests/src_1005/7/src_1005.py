def func(*args):
	
	shoes = [int(x) for x in args[0].split()]
	distinct = []
	count = 0
	for shoe in shoes:
	    if (shoe in distinct):
	        count += 1
	    else:
	        distinct.append(shoe)
	return(count)
