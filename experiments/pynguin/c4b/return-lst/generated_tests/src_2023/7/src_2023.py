def func(*args):
	ret_values = []
	
	n = int(args[0])
	test = 0
	i = 0
	j = 0
	x = True
	j = 1
	j_list = [0]
	i_list = [0]
	final_list = []
	while (test < n):
	    test = ((4 * i) + (7 * j))
	    j_list.append(j)
	    if ((n - test) < 7):
	        break
	    j += 1
	for j in j_list:
	    i = ((n - (j * 7)) / 4)
	    if i.is_integer():
	        if (((n - (j * 7)) / 4) >= 0):
	            i_list.append(int(i))
	            final_list.append((int(i), int(j)))
	if final_list:
	    final = []
	    min_sum = (10 ** 999)
	    for (a, b) in final_list:
	        if ((a + b) == min_sum):
	            final.append((a, b))
	        elif ((a + b) < min_sum):
	            final = [(a, b)]
	            min_sum = (a + b)
	    min_b = (10 ** 999)
	    a_final = 0
	    for (a, b) in final:
	        if (b < min_b):
	            min_b = b
	            a_final = a
	    ret_values.append(((str(4) * a_final) + (str(7) * min_b)))
	else:
	    ret_values.append((- 1))

	return ret_values
