def func(*args):
	ret_values = []
	
	data = str(args[0])
	list = []
	length = len(data)
	for i in range(length):
	    list.append(ord(data[i]))
	maximum = max(list)
	count = 0
	for i in range(length):
	    if (list[i] == maximum):
	        count += 1
	string = chr(maximum)
	for k in range(count):
	    ret_values.append(string, end='')

	return ret_values
