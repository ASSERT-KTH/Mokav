def func(*args):
	
	
	def cal(a, b, c):
	    if (c[0] == '+'):
	        return (int(a) + int(b))
	    return (int(a) * int(b))
	num = args[0].split()
	op = args[1].split()
	
	def DFS(l, no):
	    if (no == 3):
	        return int(l[0])
	    else:
	        ln = len(l)
	        ans = (10 ** 10)
	        for i in range(ln):
	            for j in range((i + 1), ln):
	                ll = []
	                for k in range(ln):
	                    if ((i != k) and (j != k)):
	                        ll.append(l[k])
	                ll.append(cal(l[i], l[j], op[no]))
	                ans = min(ans, DFS(ll, (no + 1)))
	        return ans
	yield(DFS(num, 0))
