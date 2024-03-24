def func(*args):
	
	l = list(map(int, args[0].split()))
	ans = (10 ** 22)
	for st in range(4):
	    for fin in range(4):
	        new_l = ([0] * 3)
	        new_l[0] = l[0]
	        new_l[1] = l[1]
	        new_l[2] = l[2]
	        if (st < 3):
	            for i in range(0, (st + 1)):
	                new_l[i] += 1
	        if (fin < 3):
	            for i in range(0, (fin + 1)):
	                new_l[i] -= 1
	        cur_ans = 0
	        for i in range(3):
	            cur_ans += abs((max(new_l) - new_l[i]))
	        ans = min(ans, cur_ans)
	return(ans)
