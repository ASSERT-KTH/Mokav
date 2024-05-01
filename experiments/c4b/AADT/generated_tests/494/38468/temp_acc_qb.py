def patched_func(*args):
	global_list = []
	
	list1 = []
	for i in range(1, 1001):
	    if (i < 10):
	        list1.append(i)
	    elif (i < 100):
	        de1 = int((i / 10))
	        de2 = (i % 10)
	        list1.append(de1)
	        list1.append(de2)
	    elif (i < 1000):
	        de1 = int((i / 100))
	        list1.append(de1)
	        de2 = int(((i - (de1 * 100)) / 10))
	        list1.append(de2)
	        de3 = ((i % 100) % 10)
	        list1.append(de3)
	n = int(args[0])
	global_list.append(list1[(n - 1)])
	return global_list