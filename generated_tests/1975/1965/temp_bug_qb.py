def original_func(*args):
	global_list = []
	
	nAndTStr = args[0]
	n = int(nAndTStr.split()[0])
	t = int(nAndTStr.split()[1])
	que = args[1]
	
	def shift1Second(theQue):
	    queque = list(theQue)
	    jump = False
	    for i in range(n):
	        if ((queque[i] == 'G') and (i > 0)):
	            if ((queque[(i - 1)] == 'B') and (not jump)):
	                queque[i] = 'B'
	                queque[(i - 1)] = 'G'
	                jump = True
	            else:
	                jump = False
	    return ''.join(queque)
	for i in range(t):
	    que = shift1Second(que)
	global_list.append(que)
	return global_list