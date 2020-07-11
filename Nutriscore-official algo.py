import math
import numpy
import scipy
from scipy import linalg


######################## POINT POSITIF ##################################
def point_fibres (fibres):
	if   fibres <= 0.9 :
		return 0
	elif fibres <= 1.9 :
		return 1
	elif fibres <= 2.8 :
		return 2
	elif fibres <= 3.7 :
		return 3
	elif fibres <= 4.7 :
		return 4
	else :
		return 5

def point_prot (proteine):
	if   proteine <= 1.6 :
		return 0
	elif proteine <= 3.2 :
		return 1
	elif proteine <= 4.8 :
		return 2
	elif proteine <= 6.4 :
		return 3
	elif proteine <= 8.0 :
		return 4
	else :
		return 5

def point_leg (legume):
	if   legume <= 40 :
		return 0
	elif legume <= 60 :
		return 1
	elif legume <= 80 :
		return 2
	else :
		return 5

def nbr_point_poistif (aliment,cal_prot):
	if cal_prot :
		return  point_fibres(aliment['fibres']) + point_prot(aliment['proteine']) + point_leg(aliment['legume'])
	else :
		return  point_fibres(aliment['fibres']) + point_leg(aliment['legume'])
	 

######################## POINT NEGATIF ##################################
def point_sel (sel):
	if   sel <= 90 :
		return 0
	elif sel <= 180 :
		return 1
	elif sel <= 270 :
		return 2
	elif sel <= 360 :
		return 3
	elif sel <= 450 :
		return 4
	elif  sel <= 540:
		return 5
	elif  sel <= 630:
		return 6
	elif  sel <= 720:
		return 7
	elif  sel <= 810:
		return 8
	elif  sel <= 900:
		return 9
	else :
		return 10

def point_sucre (sucre):
	if   sucre <= 4.5 :
		return 0
	elif sucre <= 9 :
		return 1
	elif sucre <= 13.5 :
		return 2
	elif sucre <= 18 :
		return 3
	elif sucre <= 22.5 :
		return 4
	elif sucre <= 27:
		return 5
	elif sucre <= 31:
		return 6
	elif sucre <= 36:
		return 7
	elif sucre <= 40:
		return 8
	elif sucre <= 45:
		return 9
	else :
		return 10

def point_AGS (ags):
	if   ags <= 1 :
		return 0
	elif ags <= 2 :
		return 1
	elif ags <= 3 :
		return 2
	elif ags <= 4 :
		return 3
	elif ags <= 5 :
		return 4
	elif ags <= 6:
		return 5
	elif ags <= 7:
		return 6
	elif ags <= 8:
		return 7
	elif ags <= 9:
		return 8
	elif ags <= 10:
		return 9
	else :
		return 10

def point_energie (energie):
	if   energie <= 335 :
		return 0
	elif energie <= 670 :
		return 1
	elif energie <= 1005 :
		return 2
	elif energie <= 1340 :
		return 3
	elif energie <= 1675 :
		return 4
	elif energie <= 2010:
		return 5
	elif energie <= 2345:
		return 6
	elif energie <= 2680:
		return 7
	elif energie <= 3015:
		return 8
	elif energie <= 3350:
		return 9
	else :
		return 10


def nbr_point_negatif (aliment):
	return point_sel(aliment['sel']) + point_sucre(aliment['sucre']) + point_energie(aliment['energie']) + point_AGS(aliment['AGS'])


######################## POINT TOTAL ##################################  WARNING
def score_int_to_char_aliment (note):
	if   note <= -1 : # a voire pour le moins 15
		return 'A'
	elif note <= 2 :
		return 'B'
	elif note <= 10:
		return 'C'
	elif note <=18 :
		return 'D'
	else :
		return 'E'
		
def score_int_to_char_boisson (note):
	if   note <= -1 : # a voire pour le moins 15
		return 'A'
	elif note <= 2 :
		return 'B'
	elif note <= 10:
		return 'C'
	elif note <=18 :
		return 'D'
	else :
		return 'E'

def calcl_nutriscore (aliment):
	neg = nbr_point_negatif(aliment)
	if neg >=11 and aliment['legume'] < 80  :
		pos = nbr_point_poistif(aliment,False)
	else :
		pos = nbr_point_poistif(aliment,True)
	res = neg - pos
	return res


