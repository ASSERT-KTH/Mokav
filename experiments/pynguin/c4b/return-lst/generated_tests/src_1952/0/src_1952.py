def func(*args):
	ret_values = []
	
	from sys import stdin, stdout
	
	def ri():
	    return map(int, stdin.readline().split())
	option1 = [[0, 0, 0], [1, 1, 1], [0, 1, 1], [0, 0, 1]]
	option2 = [[0, 0, 0], [1, 1, 1], [1, 1, 0], [1, 0, 0]]
	option13 = {1: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0]], 2: [[0, 0, 1], [0, 1, 0], [0, 0, 0]], 3: [[0, 0, 0]]}
	option23 = {1: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0]], 2: [[1, 0, 0], [0, 1, 0], [0, 0, 0]], 3: [[0, 0, 0]]}
	
	def findoption(m1, m2, m3):
	    ans = (10 ** 100)
	    for o1 in option1:
	        for o2 in option2:
	            mm1 = ((m1 - o1[0]) - o2[0])
	            mm2 = ((m2 - o1[1]) - o2[1])
	            mm3 = ((m3 - o1[2]) - o2[2])
	            if ((mm1 < 0) or (mm2 < 0) or (mm3 < 0)):
	                continue
	            maxm = max(mm1, mm2, mm3)
	            ans = min(ans, ((((maxm * 3) - mm1) - mm2) - mm3))
	    for i1 in option13:
	        for i2 in option23:
	            oo1 = option13[i1]
	            oo2 = option23[i2]
	            for o1 in oo1:
	                for o2 in oo2:
	                    mm1 = ((m1 - o1[0]) - o2[0])
	                    mm2 = ((m2 - o1[1]) - o2[1])
	                    mm3 = ((m3 - o1[2]) - o2[2])
	                    if ((mm1 < 0) or (mm2 < 0) or (mm3 < 0)):
	                        continue
	                    maxm = max(mm1, mm2, mm3)
	                    diff = 0
	                    for i in range(3):
	                        diff += (option1[i1][i] - o1[i])
	                        diff += (option2[i2][i] - o2[i])
	                    ans = min(ans, (((((maxm * 3) - mm1) - mm2) - mm3) + diff))
	    return ans
	(m1, m2, m3) = ri()
	if ((m1 == 0) and (m2 == 1) and (m3 == 0)):
	    ret_values.append(0)
	else:
	    ret_values.append(findoption(m1, m2, m3))

	return ret_values
