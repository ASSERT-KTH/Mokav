def original_func(*args):
	global_list = []
	
	import sys
	no = str(args[0])
	global_list.append(no)
	d = {}
	d['4'] = 0
	d['7'] = 0
	for i in no:
	    if ((i == '4') or (i == '7')):
	        d[i] += 1
	sum1 = 0
	sum1 += d['4']
	sum1 += d['7']
	li = ['4', '7']
	for i in str(sum1):
	    if (i not in li):
	        global_list.append('NO')
	        sys.exit()
	global_list.append('YES')
	return global_list