def func(*args):
	
	input = int(args[0])
	sum = 0
	temp = 0
	for i in range(input, 0, (- 1)):
	    sum += i
	for i in range(input, 0, (- 1)):
	    sum += ((i - 1) * temp)
	    temp += 1
	return(sum)
