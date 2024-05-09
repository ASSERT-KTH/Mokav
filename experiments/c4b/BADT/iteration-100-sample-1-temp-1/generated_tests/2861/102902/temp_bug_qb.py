def original_func(*args):
	global_list = []
	
	n = str(args[0])
	li = n.split(' ')
	x = int(li[0])
	y = int(li[1])
	l = int(li[2])
	r = int(li[3])
	cnt = 0
	xs = []
	ys = []
	while True:
	    tmp = (x ** cnt)
	    if (tmp < 1e+18):
	        xs.append(tmp)
	        cnt += 1
	    else:
	        break
	cnt = 0
	while True:
	    tmp = (y ** cnt)
	    if (tmp < 1e+18):
	        ys.append(tmp)
	        cnt += 1
	    else:
	        break
	years = set()
	for i in xs:
	    for j in ys:
	        years.add((i + j))
	accept = []
	for i in years:
	    if ((i >= l) and (i <= r)):
	        accept.append(i)
	accept.append((r + 1))
	mx = (- 1000000)
	for i in range(1, len(accept)):
	    if (((accept[i] - accept[(i - 1)]) - 1) > mx):
	        mx = ((accept[i] - accept[(i - 1)]) - 1)
	global_list.append(mx)
	return global_list