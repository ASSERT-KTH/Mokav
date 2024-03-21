def func(*args):
	ret_values = []
	
	aaa = 0
	
	def f(l1, r1, l2, r2, top):
	    global aaa
	    if ((l1 > r1) or (l2 > r2)):
	        return 0
	    if (((top - 1) <= aaa) or (((r1 - l1) + 1) <= aaa) or (((r2 - l2) + 1) <= aaa)):
	        return 0
	    if (top == 2):
	        return 1
	    if (l1 > top):
	        l1 -= top
	        r1 -= top
	    if (l2 > top):
	        l2 -= top
	        r2 -= top
	    if ((l1 == l2) and (r1 == r2)):
	        return ((r1 - l1) + 1)
	    if ((l1 == 0) and (r1 == (top - 1))):
	        return ((r2 - l2) + 1)
	    if ((l2 == 0) and (r2 == (top - 1))):
	        return ((r1 - l1) + 1)
	    if (((l1 <= l2) and (l2 <= r1)) or ((l2 <= l1) and (l1 <= r2))):
	        ans = ((min(r1, r2) - max(l1, l2)) + 1)
	    else:
	        ans = 0
	    top = (top // 2)
	    ans = max(ans, f(l1, min(r1, (top - 1)), l2, min(r2, (top - 1)), top))
	    ans = max(ans, f(l1, min(r1, (top - 1)), max((top + 1), l2), r2, top))
	    ans = max(ans, f(max(l1, (top + 1)), r1, l2, min(r2, (top - 1)), top))
	    ans = max(ans, f(max(l1, (top + 1)), r1, max(l2, (top + 1)), r2, top))
	    aaa = max(aaa, ans)
	    return ans
	a = args[0].split()
	ret_values.append(f(int(a[0]), int(a[1]), int(a[2]), int(a[3]), (2 ** 36)))

	return ret_values
