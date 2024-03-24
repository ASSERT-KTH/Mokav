def func(*args):
	
	import math
	'\n#include <cstdio>\n#include <iostream>\n#include <algorithm>\n\nbool isRight(int *c){\n\n    int sides[3] = {0};\n    sides[0] = (c[4] - c[2]) * (c[4] - c[2]) + (c[5] - c[3])* (c[5] - c[3]);\n    sides[1] = (c[4] - c[0]) * (c[4] - c[0]) + (c[5] - c[1])* (c[5] - c[1]);\n    sides[2] = (c[2] - c[0]) * (c[2] - c[0]) + (c[3] - c[1])* (c[3] - c[1]);\n\n    std::sort(sides, sides + 3);\n    if(sides[0] > 0 && sides[2] == sides[0] + sides[1]){return 1;}\n    else{return 0;}\n}\n\n\nint main(){\n\n    int points[6] = {0};\n    for(int k = 0; k < 6; k++){scanf("%d", points + k);}\n\n    std::string output = "NEITHER";\n    if(isRight(points)){output = "RIGHT";}\n    else{\n        for(int k = 0; k < 6; k++){\n            ++points[k];    if(isRight(points)){output = "ALMOST"; break;}\n            points[k] -= 2; if(isRight(points)){output = "ALMOST"; break;}\n            ++points[k];\n        }\n    }\n\n    std::cout << output << std::endl;\n    return 0;\n}\n'
	
	def distancia_euclidiana(x, y):
	    lados = []
	    lados.append((math.pow((x[0] - x[1]), 2) + math.pow((y[0] - y[1]), 2)))
	    lados.append((math.pow((x[0] - x[2]), 2) + math.pow((y[0] - y[2]), 2)))
	    lados.append((math.pow((x[1] - x[2]), 2) + math.pow((y[1] - y[2]), 2)))
	    return sorted(lados)
	
	def is_right(pontos):
	    distancias = distancia_euclidiana((pontos[0], pontos[2], pontos[4]), (pontos[1], pontos[3], pontos[5]))
	    return ((distancias[0] > 0) and (distancias[2] == (distancias[1] + distancias[0])))
	pontos = [int(i) for i in args[0].split()]
	resultado = 'NEITHER'
	if is_right(pontos):
	    resultado = 'RIGHT'
	else:
	    for i in range(0, 6):
	        pontos[i] += 1
	        if is_right(pontos):
	            resultado = 'ALMOST'
	            break
	        pontos[i] -= 2
	        if is_right(pontos):
	            resultado = 'ALMOST'
	            break
	        pontos[i] += 1
	return(resultado)
