def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split(' '))
	(c, d) = map(int, args[1].split(' '))
	flag = 0
	rick = []
	morty = []
	for i in range(101):
	    rick.append((b + (i * a)))
	    morty.append((d + (i * c)))
	for i in range(len(rick)):
	    if (rick[i] in morty):
	        ret_values.append(rick[i])
	        break
	    else:
	        flag += 1
	if (flag == len(rick)):
	    ret_values.append((- 1))

	return ret_values
