def func(*args):
	ret_values = []
	
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
	accept = [(l - 1), (r + 1)]
	for i in years:
	    if (l <= i <= r):
	        accept.append(i)
	accept.append((r + 1))
	mx = (- 1000000)
	accept.sort()
	for i in range(1, len(accept)):
	    if (((accept[i] - accept[(i - 1)]) - 1) > mx):
	        mx = ((accept[i] - accept[(i - 1)]) - 1)
	ret_values.append(mx)

	return ret_values
