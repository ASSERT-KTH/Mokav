def func(*args):
	
	
	def f(list4):
	    col = ['R', 'B', 'Y', 'G']
	    a = list4.index('!')
	    for j in col:
	        if (j not in list4):
	            list4[a] = j
	    return list4
	s = str(args[0])
	l = list(s)
	list1 = ['R', 'B', 'Y', 'G']
	list2 = [(- 1), (- 1), (- 1), (- 1)]
	ans = [0, 0, 0, 0]
	for i in range(len(s)):
	    if (s[i] == 'R'):
	        list2[0] = (i % 4)
	    elif (s[i] == 'B'):
	        list2[1] = (i % 4)
	    elif (s[i] == 'Y'):
	        list2[2] = (i % 4)
	    elif (s[i] == 'G'):
	        list2[3] = (i % 4)
	    if (list2.count((- 1)) == 0):
	        break
	ans1 = [0 for i in range(len(s))]
	for i in range(len(s)):
	    a = list2.index((i % 4))
	    ans1[i] = list1[a]
	ans[0] = (ans1.count('R') - l.count('R'))
	ans[1] = (ans1.count('B') - l.count('B'))
	ans[2] = (ans1.count('Y') - l.count('Y'))
	ans[3] = (ans1.count('G') - l.count('G'))
	return(*ans)
