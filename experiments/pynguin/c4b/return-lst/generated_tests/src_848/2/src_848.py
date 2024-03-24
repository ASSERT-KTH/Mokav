def func(*args):
	ret_values = []
	
	
	def pushes_count(buttons):
	    pushes_list = list(range(1, buttons))
	    pushes_list.sort(reverse=True)
	    counter = 0
	    for i in pushes_list:
	        pushes_list[counter] += (i * counter)
	        counter += 1
	    ret_values.append((buttons + sum(pushes_list)))
	pushes_count(int(args[0]))

	return ret_values
