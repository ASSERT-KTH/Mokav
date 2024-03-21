def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    N = int(args[0])
	    S = args[1].split(':')
	    H = S[0]
	    M = S[1]
	    res = 114514
	    ans = ''
	    if (N == 12):
	        for i in range(1, 13):
	            for j in range(0, 60):
	                h = str(i)
	                m = str(j)
	                while (len(h) != 2):
	                    h = ('0' + h)
	                while (len(m) != 2):
	                    m = ('0' + m)
	                diff = 0
	                for (x, y) in zip(h, H):
	                    if (x != y):
	                        diff += 1
	                for (x, y) in zip(m, M):
	                    if (x != y):
	                        diff += 1
	                if (diff < res):
	                    res = diff
	                    ans = ((h + ':') + m)
	    else:
	        for i in range(0, 24):
	            for j in range(0, 60):
	                h = str(i)
	                m = str(j)
	                while (len(h) != 2):
	                    h = ('0' + h)
	                while (len(m) != 2):
	                    m = ('0' + m)
	                diff = 0
	                for (x, y) in zip(h, H):
	                    if (x != y):
	                        diff += 1
	                for (x, y) in zip(m, M):
	                    if (x != y):
	                        diff += 1
	                if (diff < res):
	                    res = diff
	                    ans = ((h + ':') + m)
	    ret_values.append(ans)

	return ret_values
