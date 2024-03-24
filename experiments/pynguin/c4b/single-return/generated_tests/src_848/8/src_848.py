def func(*args):
	
	
	def pushes_count(buttons):
	    pushes_list = list(range(1, buttons))
	    pushes_list.sort(reverse=True)
	    counter = 0
	    for i in pushes_list:
	        pushes_list[counter] += (i * counter)
	        counter += 1
	    return((buttons + sum(pushes_list)))
	pushes_count(int(args[0]))
