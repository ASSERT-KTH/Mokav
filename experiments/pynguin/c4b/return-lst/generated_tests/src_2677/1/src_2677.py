def func(*args):
	ret_values = []
	
	str1 = args[0]
	firststr = str1[0]
	secondstr = str1[2]
	num = int(args[1])
	
	def switch(x):
	    if (x == 'v'):
	        return 1
	    if (x == '<'):
	        return 2
	    if (x == '^'):
	        return 3
	    if (x == '>'):
	        return 4
	fsn = switch(firststr)
	ssn = switch(secondstr)
	output = 'undefined'
	num = (num % 4)
	flag1 = 0
	flag2 = 0
	if (num == 0):
	    num = 4
	fsnnum = (fsn + num)
	if ((fsn + num) > 4):
	    fsnnum = ((fsn + num) - 4)
	if (fsnnum == ssn):
	    output = 'cw'
	    flag1 = 1
	if (((fsn - num) == ((- 4) + ssn)) or ((fsn - num) == ssn)):
	    output = 'ccw'
	    flag2 = 1
	if (flag1 == flag2):
	    output = 'undefined'
	ret_values.append(output)

	return ret_values
