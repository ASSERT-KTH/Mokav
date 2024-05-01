def patched_func(*args):
	global_list = []
	
	
	def read():
	    S = args[0]
	    sList = S.split()
	    sList = [int(_) for _ in sList]
	    c = sList[0]
	    v0 = sList[1]
	    v1 = sList[2]
	    a = sList[3]
	    l = sList[4]
	    red = 0
	    cnt = 0
	    while (c > red):
	        if (cnt >= 1):
	            red -= l
	        red += v0
	        if (v0 < v1):
	            v0 += a
	        if (v0 > v1):
	            v0 = v1
	        cnt += 1
	    global_list.append(cnt)
	read()
	return global_list