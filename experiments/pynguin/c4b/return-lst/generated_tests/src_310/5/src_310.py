def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    line = str(args[0])
	    s = len(line)
	    rest = 0
	    candi = list()
	    for i in range((s - 1)):
	        if (line[i:(i + 2)] == 'VK'):
	            rest += 1
	            candi.append(i)
	            candi.append((i + 2))
	    candi = (([0] + candi) + [s])
	    s = len(candi)
	    flag = False
	    for i in range((s - 1)):
	        refer = line[candi[i]:candi[(i + 1)]]
	        if (('VV' in refer) or ('KK' in refer)):
	            flag = True
	    ret_values.append((rest + (1 if flag else 0)))

	return ret_values
