def original_func(*args):
	global_list = []
	
	import sys
	
	def calc(v, x, w):
	    if (x == 0):
	        return 0
	    return max(((v // 10) * 3), ((v - ((v // 250) * x)) - (50 * w)))
	score = [500, 1000, 1500, 2000, 2500]
	m = [int(x) for x in args[0].split()]
	w = [int(x) for x in args[1].split()]
	(hs, hw) = map(int, args[2].split())
	ans = 0
	for i in range(5):
	    ans += calc(score[i], m[i], w[i])
	ans += ((hs * 100) - (50 * hw))
	global_list.append(ans)
	return global_list