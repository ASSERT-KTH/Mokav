def func(*args):
	ret_values = []
	
	(n, m) = args[0].split(':')
	(N, M) = map(int, [n, m])
	
	def PalindromicFind(N, M):
	    indicator = False
	    for i in range(N, 24):
	        if (i == N):
	            for j in range((M + 1), 60):
	                I = str(i).zfill(2)
	                J = str(j).zfill(2)
	                if ((I[0] == J[1]) and (I[1] == J[0])):
	                    ret_values.append(((I + ':') + J))
	                    indicator = True
	                    break
	        else:
	            for j in range(0, 60):
	                I = str(i).zfill(2)
	                J = str(j).zfill(2)
	                if ((I[0] == J[1]) and (I[1] == J[0])):
	                    ret_values.append(((I + ':') + J))
	                    indicator = True
	                    break
	        if indicator:
	            break
	if ((N == 23) and (M > 32)):
	    PalindromicFind(0, (- 1))
	else:
	    PalindromicFind(N, M)

	return ret_values
