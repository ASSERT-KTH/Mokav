def original_func(*args):
	global_list = []
	
	l1 = list(map(int, args[0].split()))
	l2 = list(map(int, args[1].split()))
	
	def magicspheres(list1, list2):
	    excess_demand = [(b - a) for (a, b) in zip(list1, list2)]
	    for i in range(3):
	        if (excess_demand[i] > 0):
	            for j in range(3):
	                if (excess_demand[j] <= (- 2)):
	                    list1[i] += 1
	                    list1[j] -= 2
	                    excess_demand = [(b - a) for (a, b) in zip(list1, list2)]
	    for i in range(3):
	        if (excess_demand[i] > 0):
	            return 'No'
	    return 'Yes'
	global_list.append(magicspheres(l1, l2))
	return global_list