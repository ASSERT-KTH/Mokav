def patched_func(*args):
	global_list = []
	
	year = args[0]
	
	def check(year):
	    arr = [False for i in range(10)]
	    for i in range(len(year)):
	        if (arr[(ord(year[i]) - ord('0'))] is True):
	            return False
	        else:
	            arr[(ord(year[i]) - ord('0'))] = True
	    return True
	i = (int(year) + 1)
	while True:
	    if (check(str(i)) is True):
	        global_list.append(i)
	        break
	    else:
	        i += 1
	return global_list