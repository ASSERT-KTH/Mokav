def original_func(*args):
	global_list = []
	
	inp = int(args[0])
	prime = list()
	count = 0
	for i in range(2, (inp + 1)):
	    ans = 0
	    for j in range(2, (i - 1)):
	        if ((i % j) == 0):
	            ans = (ans + 1)
	    if (ans == 0):
	        prime.append(i)
	for i in range((inp + 1)):
	    ans = 0
	    for j in prime:
	        if ((i % j) == 0):
	            ans = (ans + 1)
	    if (ans == 2):
	        count += 1
	global_list.append(count)
	return global_list