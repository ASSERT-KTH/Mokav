def func(*args):
	ret_values = []
	
	target_height = int(args[0])
	growth = sorted([int(x) for x in args[1].split(' ')], reverse=True)
	months = 0
	while ((sum(growth[0:months]) < target_height) and (months < 12)):
	    months += 1
	if (sum(growth[0:months]) < target_height):
	    ret_values.append((- 1))
	else:
	    ret_values.append(months)

	return ret_values
