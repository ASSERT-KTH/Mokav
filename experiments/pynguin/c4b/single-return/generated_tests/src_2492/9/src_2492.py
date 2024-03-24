def func(*args):
	
	entrada = args[0].split(' ')
	listae = list(map(int, entrada))
	stock = 1
	while ((((listae[0] * stock) + listae[1]) <= listae[3]) and (listae[2] > 0)):
	    stock = ((listae[0] * stock) + listae[1])
	    listae[2] -= 1
	return(listae[2])
