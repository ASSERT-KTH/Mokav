def func(*args):
	ret_values = []
	
	
	def __init__(x, y, l, r):
	    n = (lambda a, b: ((x ** a) + (y ** b)))
	    bad = set()
	    for a in range(60):
	        for b in range(60):
	            year = n(a, b)
	            if (l <= year <= r):
	                bad.add(year)
	            elif (year > (r + 1)):
	                break
	    record = 0
	    bad = list(bad)
	    bad.append((r + 1))
	    bad.append((l - 1))
	    bad.sort()
	    if (len(bad) > 2):
	        for i in range((len(bad) - 1)):
	            score = (bad[(i + 1)] - bad[i])
	            if (score > record):
	                record = (score - 1)
	        return record
	    else:
	        return ((r - l) + 1)
	if (__name__ == '__main__'):
	    __test__ = 0
	    if __test__:
	        tests = [[1, [2, 3, 1, 10]], [8, [3, 5, 10, 22]], [0, [2, 3, 3, 5]], [1, [2, 2, 1, 10]], [213568, [2, 2, 1, 1000000]], [144115188075855871, [2, 2, 1, 1000000000000000000]], [206415, [2, 3, 1, 1000000]], [261485717957290893, [2, 3, 1, 1000000000000000000]], [933334, [12345, 54321, 1, 1000000]], [976614248345331214, [54321, 12345, 1, 1000000000000000000]], [188286357653, [2, 3, 100000000, 1000000000000]], [0, [2, 14, 732028847861235712, 732028847861235712]], [1, [14, 2, 732028847861235713, 732028847861235713]], [1, [3, 2, 6, 7]]]
	        for i in range(len(tests)):
	            ret_values.append((i + 1), end='\t')
	            ret_values.append((tests[i][0] == __init__(*tests[i][1])), end='\t')
	            ret_values.append(tests[i][0], '<<', __init__(*tests[i][1]))
	        exit()
	    ret_values.append(__init__(*map(int, args[0].split())))

	return ret_values
