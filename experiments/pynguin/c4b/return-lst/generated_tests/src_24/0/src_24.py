def func(*args):
	ret_values = []
	
	t = list(map(int, args[0].split()))
	ws = list(map(int, args[1].split()))
	(hs, hu) = map(int, args[2].split())
	res = 0
	for (minu, wrongs, punt) in zip(t, ws, [500, 1000, 1500, 2000, 2500]):
	    res += max((0.3 * punt), (((1 - (minu / 250)) * punt) - (50 * wrongs)))
	ret_values.append(int((res + ((hs * 100) + (hu * (- 50))))))

	return ret_values
