def original_func(*args):
	global_list = []
	
	s = list(map(int, args[0].split()))
	t = list(map(int, args[1].split()))
	xs = [(s[i] - t[i]) for i in range(len(s))]
	demand = []
	supply = []
	for x in xs:
	    if (x < 0):
	        demand.append((- x))
	    else:
	        supply.append(x)
	res = True
	if len(demand):
	    res = (sum(supply) >= (sum(demand) * 2))
	    if (res and (len(supply) == 2) and ((supply[0] % 2) == (supply[1] % 2) == 1)):
	        res = False
	global_list.append(('Yes' if res else 'No'))
	return global_list