def patched_func(*args):
	global_list = []
	
	length = args[0].split()
	result = ''
	for i in range(4):
	    length[i] = int(length[i])
	
	def isTriangle(l):
	    if (((l[0] + l[1]) > l[2]) and (abs((l[0] - l[1])) < l[2])):
	        return 'TRIANGLE'
	    elif ((l[0] + l[1]) == l[2]):
	        return 'SEGMENT'
	    else:
	        return 'IMPOSSIBLE'
	for i in length:
	    newLen = length[:]
	    newLen.remove(i)
	    newLen.sort()
	    if (isTriangle(newLen) == 'TRIANGLE'):
	        result = 'TRIANGLE'
	        break
	    elif ((isTriangle(newLen) == 'SEGMENT') and (result != 'TRIANGLE')):
	        result = 'SEGMENT'
	    elif (result != 'SEGMENT'):
	        result = 'IMPOSSIBLE'
	global_list.append(result)
	return global_list