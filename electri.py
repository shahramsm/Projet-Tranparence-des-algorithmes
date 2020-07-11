import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv('datas.csv')
data = data.drop_duplicates()
df2 = data.dropna()
df=df2.drop(df2.columns[[0]], axis=1, inplace=False)
df_res = df2
df_res=df_res.drop(columns=['Énergie','Fibres','Protéines','Acides gras saturés', 'Sucre', 'Sodium'])
df=df.rename(columns={"Énergie": "en", "Fibres": "fi" , 'Protéines':'pr','Acides gras saturés':'ac','Sucre':'su','Sodium':'so'})
df.sort_values(by='NutriScore')

# ANALYSE DU DATASET

df.mean()

df_var=df.drop(columns=['produit']).var()
df_var

df_max=df.drop(columns=['produit']).max()
df_max

df_min=df.drop(columns=['produit']).min()
df_min

# DEFINITION DES CONSTANTES

tmp_en = df_max['en']/5
tmp_fi = df_max['fi']/5
tmp_pr = df_max['pr']/5
tmp_ac = df_max['ac']/5
tmp_su = df_max['su']/5
tmp_so = df_max['so']/5

#minimiser
b_en = {'b1': -1,'b2': tmp_en,'b3': 2*tmp_en,'b4': 3*tmp_en,'b5': 4*tmp_en,'b6': 1000000}
b_ac = {'b1': -1,'b2': tmp_ac,'b3': 2*tmp_ac,'b4': 3*tmp_ac,'b5': 4*tmp_ac,'b6': 1000000}
b_su = {'b1': -1,'b2': tmp_su,'b3': 2*tmp_su,'b4': 3*tmp_su,'b5': 4*tmp_su,'b6': 1000000}
b_so = {'b1': -1,'b2': tmp_so,'b3': 2*tmp_so,'b4': 3*tmp_so,'b5': 4*tmp_so,'b6': 1000000}

#maximiser
b_fi = {'b1': 1000000,'b2': 4*tmp_fi,'b3': 3*tmp_fi,'b4': 2*tmp_fi,'b5': tmp_fi,'b6': -1}
b_pr = {'b1': 1000000,'b2': 4*tmp_pr,'b3': 3*tmp_pr,'b4': 2*tmp_pr,'b5': tmp_pr,'b6': -1}

k_en = 2
k_fi = 0.5
k_pr = 0.5
k_ac = 1
k_su = 1
k_so = 1
k_somme = k_en + k_fi + k_pr + k_ac + k_su + k_so

# ALGO

def concordance_en(en):
    c1 = 1 if en<=b_en['b1'] else 0
    c2 = 1 if en<=b_en['b2'] else 0
    c3 = 1 if en<=b_en['b3'] else 0
    c4 = 1 if en<=b_en['b4'] else 0
    c5 = 1 if en<=b_en['b5'] else 0
    c6 = 1 if en<=b_en['b6'] else 0
    return {'c1':c1, 'c2':c2, 'c3':c3, 'c4':c4, 'c5':c5, 'c6':c6 }

def concordance_fi(fi):
    c1 = 0 if fi<=b_fi['b1'] else 1
    c2 = 0 if fi<=b_fi['b2'] else 1
    c3 = 0 if fi<=b_fi['b3'] else 1
    c4 = 0 if fi<=b_fi['b4'] else 1
    c5 = 0 if fi<=b_fi['b5'] else 1
    c6 = 0 if fi<=b_fi['b6'] else 1
    return {'c1':c1, 'c2':c2, 'c3':c3, 'c4':c4, 'c5':c5, 'c6':c6 }

def concordance_pr(pr):
    c1 = 0 if pr<=b_pr['b1'] else 1
    c2 = 0 if pr<=b_pr['b2'] else 1
    c3 = 0 if pr<=b_pr['b3'] else 1
    c4 = 0 if pr<=b_pr['b4'] else 1
    c5 = 0 if pr<=b_pr['b5'] else 1
    c6 = 0 if pr<=b_pr['b6'] else 1
    return {'c1':c1, 'c2':c2, 'c3':c3, 'c4':c4, 'c5':c5, 'c6':c6 }

def concordance_ac(ac):
    c1 = 1 if ac<=b_ac['b1'] else 0
    c2 = 1 if ac<=b_ac['b2'] else 0
    c3 = 1 if ac<=b_ac['b3'] else 0
    c4 = 1 if ac<=b_ac['b4'] else 0
    c5 = 1 if ac<=b_ac['b5'] else 0
    c6 = 1 if ac<=b_ac['b6'] else 0
    return {'c1':c1, 'c2':c2, 'c3':c3, 'c4':c4, 'c5':c5, 'c6':c6 }

def concordance_su(su):
    c1 = 1 if su<=b_su['b1'] else 0
    c2 = 1 if su<=b_su['b2'] else 0
    c3 = 1 if su<=b_su['b3'] else 0
    c4 = 1 if su<=b_su['b4'] else 0
    c5 = 1 if su<=b_su['b5'] else 0
    c6 = 1 if su<=b_su['b6'] else 0
    return {'c1':c1, 'c2':c2, 'c3':c3, 'c4':c4, 'c5':c5, 'c6':c6 }

def concordance_so(so):
    c1 = 1 if so<=b_so['b1'] else 0
    c2 = 1 if so<=b_so['b2'] else 0
    c3 = 1 if so<=b_so['b3'] else 0
    c4 = 1 if so<=b_so['b4'] else 0
    c5 = 1 if so<=b_so['b5'] else 0
    c6 = 1 if so<=b_so['b6'] else 0
    return {'c1':c1, 'c2':c2, 'c3':c3, 'c4':c4, 'c5':c5, 'c6':c6 }

def concordance_partiel(row):
    en = concordance_en(row['en'])
    fi = concordance_fi(row['fi'])
    pr = concordance_pr(row['pr'])
    ac = concordance_ac(row['ac'])
    su = concordance_su(row['su'])
    so = concordance_so(row['so'])
    return {'en':en, 'fi':fi, 'pr':pr, 'ac':ac, 'su':su, 'so':so}
    
    
def concordance_global(row):
    C = concordance_partiel(row)
    c1 = (k_en*C['en']['c1'] + k_fi*C['fi']['c1'] + k_pr*C['pr']['c1'] + k_ac*C['ac']['c1'] + k_su*C['su']['c1'] + k_so*C['so']['c1'])/(k_somme)
    c2 = (k_en*C['en']['c2'] + k_fi*C['fi']['c2'] + k_pr*C['pr']['c2'] + k_ac*C['ac']['c2'] + k_su*C['su']['c2'] + k_so*C['so']['c2'])/(k_somme)
    c3 = (k_en*C['en']['c3'] + k_fi*C['fi']['c3'] + k_pr*C['pr']['c3'] + k_ac*C['ac']['c3'] + k_su*C['su']['c3'] + k_so*C['so']['c3'])/(k_somme)
    c4 = (k_en*C['en']['c4'] + k_fi*C['fi']['c4'] + k_pr*C['pr']['c4'] + k_ac*C['ac']['c4'] + k_su*C['su']['c4'] + k_so*C['so']['c4'])/(k_somme)
    c5 = (k_en*C['en']['c5'] + k_fi*C['fi']['c5'] + k_pr*C['pr']['c5'] + k_ac*C['ac']['c5'] + k_su*C['su']['c5'] + k_so*C['so']['c5'])/(k_somme)
    c6 = (k_en*C['en']['c6'] + k_fi*C['fi']['c6'] + k_pr*C['pr']['c6'] + k_ac*C['ac']['c6'] + k_su*C['su']['c6'] + k_so*C['so']['c6'])/(k_somme)
    return {'c1':c1, 'c2':c2, 'c3':c3, 'c4':c4, 'c5':c5, 'c6':c6 }

def relation_surclassement(row):
    res=concordance_global(row)
    if res['c2']>=0.5:
        return 'A'
    elif res['c3']>=0.5:
        return 'B'
    elif res['c4']>=0.5:
        return 'C'
    if res['c5']>=0.5:
        return 'D'
    else : 
        return 'E'
    
def electrie():
    res=[]
    for index, row in df.iterrows():
        res.append(relation_surclassement(row))
    return res


df_res['electri']=electrie()

df_res.sort_values(by='NutriScore')

err = 0
nbr = 0
err_bis = 0
def test(s):
    return (s=='AB' or s=='BA' or s=='BC' or s=='CB' or s=='CD' or s=='DC' or s=='DE' or s=='ED')
        
for ind , row in df_res.iterrows():
    nbr = nbr + 1
    if row['NutriScore']==row['electri']:
        err = err + 1
        
print('nbr erreur : ',err,' sur ',nbr)
print('nbr erreur a un près : ',err_bis,' sur ',nbr)                                    