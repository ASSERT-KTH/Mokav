def func(*args):
	
	(a, b, c, d, e) = map(int, args[0].split())
	(f, g, h, i, j) = map(int, args[1].split())
	(k, l, m, n, o) = map(int, args[2].split())
	(p, q, r, s, t) = map(int, args[3].split())
	(u, v, w, x, y) = map(int, args[4].split())
	F = [[a, b, c, d, e], [f, g, h, i, j], [k, l, m, n, o], [p, q, r, s, t], [u, v, w, x, y]]
	V = 0
	while (V < 5):
	    A = F[0][V]
	    if (A == 1):
	        P = 0
	        H = V
	    V = (V + 1)
	W = 0
	while (W < 5):
	    B = F[1][W]
	    if (B == 1):
	        P = 1
	        H = W
	    W = (W + 1)
	X = 0
	while (X < 5):
	    C = F[2][X]
	    if (C == 1):
	        P = 2
	        H = X
	    X = (X + 1)
	Y = 0
	while (Y < 5):
	    D = F[3][Y]
	    if (D == 1):
	        P = 3
	        H = Y
	    Y = (Y + 1)
	Z = 0
	while (Z < 5):
	    E = F[4][Z]
	    if (E == 1):
	        P = 4
	        H = Z
	    Z = (Z + 1)
	G = abs((2 - P))
	T = abs((2 - H))
	J = (G + T)
	return(J)
