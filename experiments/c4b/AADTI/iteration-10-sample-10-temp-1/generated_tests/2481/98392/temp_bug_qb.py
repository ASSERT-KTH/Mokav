def original_func(*args):
	global_list = []
	
	n = int(args[0])
	queue = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	rotate = 0
	actQue = ((2 ** rotate) * 5)
	if (n <= 5):
	    ans = queue[int((n - 1))]
	else:
	    while (n > actQue):
	        rotate += 1
	        actQue = ((2 ** rotate) * 5)
	    else:
	        rotate += (- 1)
	        actQue = ((2 ** rotate) * 5)
	        if (n == (actQue - 1)):
	            ans = queue[(- 1)]
	        else:
	            n = (n - actQue)
	            if (rotate == 0):
	                for i in range(5):
	                    if (n <= ((2 ** (rotate + 1)) * (i + 1))):
	                        ans = queue[i]
	                        break
	            else:
	                for i in range(5):
	                    if (n <= ((2 ** rotate) * (i + 1))):
	                        ans = queue[i]
	                        break
	global_list.append(ans)
	return global_list