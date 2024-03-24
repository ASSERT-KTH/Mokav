def func(*args):
	
	gl = [args[0] for i in range(8)]
	cnt = 0
	for i in range(8):
	    if (gl[i][0] == gl[i][1] == gl[i][2] == gl[i][3] == gl[i][4] == gl[i][5] == gl[i][6] == gl[i][7] == 'B'):
	        cnt += 1
	    if (gl[0][i] == gl[1][i] == gl[2][i] == gl[3][i] == gl[4][i] == gl[5][i] == gl[6][i] == gl[7][i] == 'B'):
	        cnt += 1
	if (cnt == 16):
	    cnt = 8
	return(cnt)
