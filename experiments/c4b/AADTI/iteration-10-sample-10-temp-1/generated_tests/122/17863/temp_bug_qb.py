def original_func(*args):
	global_list = []
	
	i = list(args[0].split(' '))
	j = list(args[1].split(' '))
	w = list(args[2].split(' '))
	max = [500, 1000, 1500, 2000, 2500]
	count = 0
	ans = 0
	for count in range(5):
	    t = int((((1 - (int(i[count]) / 250)) * int(max[count])) - (50 * int(j[count]))))
	    ans1 = 0
	    ans1 = int((0.3 * int(max[count])))
	    if (ans1 > t):
	        ans += ans1
	    else:
	        ans += t
	ans += ((100 * int(w[0])) - (50 * int(w[1])))
	global_list.append(ans)
	return global_list