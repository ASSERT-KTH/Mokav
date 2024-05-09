def original_func(*args):
	global_list = []
	
	size = int(args[0])
	string = args[1]
	answer = []
	list_ = list(string)
	memory = 1
	counter = 0
	for i in range(0, size):
	    if (int(list_[i]) == memory):
	        counter += memory
	    else:
	        answer.append(counter)
	        counter = 0
	        if (memory == 1):
	            memory = 0
	            counter += memory
	        else:
	            memory = 1
	            counter += memory
	answer.append(counter)
	mystring = ''
	for digit in answer:
	    mystring += str(digit)
	global_list.append(mystring)
	return global_list