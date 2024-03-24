def func(*args):
	
	size = int(args[0])
	string = args[1]
	list_ = list(string)
	answer = []
	counter = 0
	for i in range(0, size):
	    if (list_[i] == '1'):
	        counter += 1
	    else:
	        answer.append(counter)
	        counter = 0
	answer.append(counter)
	mystring = ''
	for digit in answer:
	    mystring += str(digit)
	return(mystring)
