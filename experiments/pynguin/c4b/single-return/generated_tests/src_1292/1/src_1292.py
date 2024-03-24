def func(*args):
	
	import math
	
	def get_cnt(res):
	    n = (1 + math.floor(math.sqrt((2 * res))))
	    if (((n * (n - 1)) / 2) == res):
	        return n
	    else:
	        return (- 1)
	
	def calc():
	    cnt = list(map(int, args[0].split()))
	    if (cnt == [0, 0, 0, 0]):
	        return '0'
	    a = get_cnt(cnt[0])
	    b = get_cnt(cnt[3])
	    if (cnt == [0, 0, 0, cnt[3]]):
	        a = 0
	    if (cnt == [cnt[0], 0, 0, 0]):
	        b = 0
	    if ((a == (- 1)) or (b == (- 1)) or ((a * b) != (cnt[1] + cnt[2]))):
	        return 'Impossible'
	    ans = (['0'] * (a + b))
	    i = 0
	    while (b > 0):
	        while (cnt[1] >= b):
	            i = (i + 1)
	            cnt[1] -= b
	        b -= 1
	        ans[i] = '1'
	        i += 1
	    return ''.join(ans)
	return(calc())
