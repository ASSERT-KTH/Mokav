def func(*args):
	ret_values = []
	
	import sys
	import math
	(h, m) = [int(x) for x in sys.stdin.readline().split(':')]
	if ((h >= 0) and (h < 5)):
	    if ((h * 10) <= m):
	        h += 1
	    m = (h * 10)
	    ret_values.append(((('0' + str(h)) + ':') + str(m)))
	elif ((h >= 10) and (h < 15)):
	    if ((((h % 10) * 10) + 1) <= m):
	        h += 1
	    m = (((h % 10) * 10) + 1)
	    ret_values.append(((str(h) + ':') + str(m)))
	elif ((h >= 20) and (h < 23)):
	    if ((((h % 10) * 10) + int((h / 10))) <= m):
	        h += 1
	    m = (((h % 10) * 10) + int((h / 10)))
	    ret_values.append(((str(h) + ':') + str(m)))
	elif ((h > 5) and (h < 10)):
	    ret_values.append('10:01')
	elif ((h > 15) and (h < 20)):
	    ret_values.append('20:02')
	elif (h == 5):
	    if (m < 50):
	        ret_values.append('05:50')
	    else:
	        ret_values.append('10:01')
	elif (h == 15):
	    if (m < 51):
	        ret_values.append('15:51')
	    else:
	        ret_values.append('20:02')
	elif (h == 23):
	    if (m < 32):
	        ret_values.append('23:32')
	    else:
	        ret_values.append('00:00')

	return ret_values
