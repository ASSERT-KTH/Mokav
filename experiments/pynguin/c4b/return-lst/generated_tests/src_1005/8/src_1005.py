def func(*args):
	ret_values = []
	
	shoes = [int(x) for x in args[0].split()]
	distinct = []
	count = 0
	for shoe in shoes:
	    if (shoe in distinct):
	        count += 1
	    else:
	        distinct.append(shoe)
	ret_values.append(count)

	return ret_values
