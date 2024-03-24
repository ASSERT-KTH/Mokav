def func(*args):
	ret_values = []
	
	count = int(args[0])
	data = {1: 'Sheldon', 2: 'Leonard', 3: 'Penny', 4: 'Rajesh', 5: 'Howard'}
	position = 1
	stepin = 0
	k = 1
	while True:
	    if ((count >= position) and (count < (position + (2 ** stepin)))):
	        ret_values.append(data[k])
	        break
	    position += (2 ** stepin)
	    if (k == 5):
	        stepin += 1
	        k = 1
	    else:
	        k += 1

	return ret_values
