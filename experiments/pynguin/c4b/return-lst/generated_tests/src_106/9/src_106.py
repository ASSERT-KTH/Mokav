def func(*args):
	ret_values = []
	
	l1 = list(map(int, args[0].split()))
	l2 = list(map(int, args[1].split()))
	
	def magicspheres(list1, list2):
	    excess_demand = [(b - a) for (a, b) in zip(list1, list2)]
	
	    def valid_supply():
	        for i in range(3):
	            if (excess_demand[i] <= (- 2)):
	                return i
	        return (- 1)
	    for i in range(3):
	        if (excess_demand[i] > 0):
	            j = valid_supply()
	            while ((j != (- 1)) and (excess_demand[i] > 0)):
	                list1[i] += 1
	                list1[j] -= 2
	                excess_demand = [(b - a) for (a, b) in zip(list1, list2)]
	                j = valid_supply()
	    for i in range(3):
	        if (excess_demand[i] > 0):
	            return 'No'
	    return 'Yes'
	ret_values.append(magicspheres(l1, l2))

	return ret_values
