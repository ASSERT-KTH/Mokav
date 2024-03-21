def func(*args):
	ret_values = []
	
	l = list(map(int, args[0].split()))
	l1 = list(map(int, args[1].split()))
	k = 0
	k1 = 0
	k2 = 0
	k3 = 0
	if ((l[0] - l1[0]) < 0):
	    k = (k + abs((l[0] - l1[0])))
	else:
	    k1 = (k1 + abs((l[0] - l1[0])))
	if ((l[1] - l1[1]) < 0):
	    k = (k + abs((l[1] - l1[1])))
	else:
	    k2 = (k2 + abs((l[1] - l1[1])))
	if ((l[2] - l1[2]) < 0):
	    k = (k + abs((l[2] - l1[2])))
	else:
	    k3 = (k3 + abs((l[2] - l1[2])))
	kil = 0
	kil = (kil + (k1 // 2))
	kil = (kil + (k2 // 2))
	kil = (kil + (k3 // 2))
	if (kil >= k):
	    ret_values.append('Yes')
	else:
	    ret_values.append('No')

	return ret_values
