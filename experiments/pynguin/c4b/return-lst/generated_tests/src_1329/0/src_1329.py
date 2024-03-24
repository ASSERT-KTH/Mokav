def func(*args):
	ret_values = []
	
	t = list(map(int, args[0].strip().split(' ')))
	w = list(map(int, args[1].strip().split(' ')))
	h = list(map(int, args[2].strip().split(' ')))
	ans = 0
	for i in range(5):
	    x = (500 * (i + 1))
	    ans += max(int((0.3 * x)), ((x - ((x * t[i]) // 250)) - (50 * w[i])))
	ans += (100 * h[0])
	ans -= (50 * h[1])
	ret_values.append(ans)

	return ret_values
