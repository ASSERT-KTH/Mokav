def func(*args):
	
	'\nCreated on 12/08/2017\n\n@author: ernesto\n'
	import logging
	from collections import Counter
	from functools import reduce
	import sys
	nivel_log = logging.ERROR
	logger_cagada = None
	
	def verga_core(tam_liston, tam_cortes):
	    tamanos_parciales_liston = ([(- (4000 * 8000))] * (tam_liston + 1))
	    tamanos_parciales_liston[0] = 0
	    tam_cortes_ord = sorted(set(filter((lambda x: (x <= tam_liston)), tam_cortes)))
	    if ((not tam_cortes_ord) or (tam_cortes_ord[(- 1)] > tam_liston)):
	        return 0
	    for tam_corte in tam_cortes_ord:
	        for tam_corte_1 in tam_cortes_ord:
	            if (not (tam_corte % tam_corte_1)):
	                tamanos_parciales_liston[tam_corte] = (tam_corte // tam_corte_1)
	                break
	    logger_cagada.debug('los tams de cortes {}'.format(tamanos_parciales_liston))
	    for tam_parcial_liston in range((tam_cortes_ord[0] + 1), (tam_liston + 1)):
	        lista_valores = [(tamanos_parciales_liston[(tam_parcial_liston - tam_corte)] + 1) for tam_corte in tam_cortes_ord if (tam_corte <= tam_parcial_liston)]
	        if lista_valores:
	            tamanos_parciales_liston[tam_parcial_liston] = max(lista_valores)
	    logger_cagada.debug('los tams parciales {}'.format(tamanos_parciales_liston))
	    return tamanos_parciales_liston[tam_liston]
	
	def verga_main():
	    lineas = list(sys.stdin)
	    (tam_liston, tam_corte_1, tam_corte_2, tam_corte_3) = [int(x) for x in lineas[0].strip().split(' ')]
	    caca = verga_core(tam_liston, (tam_corte_1, tam_corte_2, tam_corte_3))
	    return(caca)
	if (__name__ == '__main__'):
	    FORMAT = '[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s'
	    logging.basicConfig(level=nivel_log, format=FORMAT)
	    logger_cagada = logging.getLogger('asa')
	    logger_cagada.setLevel(nivel_log)
	    verga_main()
