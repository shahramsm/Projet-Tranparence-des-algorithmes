# -*- coding: utf-8 -*-
# import PuLP

from pulp import*

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
data = pd.read_csv('datas.csv')
data = data.drop_duplicates()
df1 = data.dropna()


# Create the 'prob' variable to contain the problem data
prob1 = LpProblem("The Nutriscore_final", LpMaximize)
ls2=[]
# Create problem variables
for i in range(50):
    globals()['x_'+str(i)]=LpVariable("aliment_"+str(i),0,120)
    ls2.append(globals()['x_'+str(i)])
#print(ls2)    
ls1=[]  
# Ecarts pour les classes
for i in range(4):
    globals()['epsilon_'+str(i)]=LpVariable("epsilon_"+str(i),1,120)
    ls1.append(globals()['epsilon_'+str(i)])
    
# Ecarts entre les utilités
for i in range(49):
    globals()['alpha_'+str(i)]=LpVariable("alpha_"+str(i),0.001,120)
    ls1.append(globals()['alpha_'+str(i)])
"""
for i in range(6):
    globals()['beta_'+str(i)]=LpVariable("beta_"+str(i),0,120)
    ls1.append(globals()['beta_'+str(i)])
"""
df2=df1.drop(df1.columns[[1]], axis='columns') 
df3=df2[:50]

df3.index = range(50)
print(df3)
m=df3.values
#print(m)

# Variables associés aux fonctions d'utilités marginales de l'aliment 1
U_dict = dict()

for i in range(len(m)):
    ls=[]
    for j in range(len(m[i])):
        if j !=0 and j !=len(m[i])-1:
            globals()['U_'+str(m[i][j])]=LpVariable("utilite_"+str(j)+"_alim_"+str(i),0,20)
            ls.append(globals()['U_'+str(m[i][j])])
    U_dict["list des utilité "+str(i)] = ls
          
    
#print (U_dict)

def sum2(l):
    su2=None
    for i in l:
        su2=su2+i
    return su2
    
# The objective function is added to 'prob' first
prob1 +=sum2(ls1), "Health restored; to be maximized"
#print(prob1)

for i in range(50):
    prob1 += sum2(U_dict.get("list des utilité "+str(i)))==ls2[i], "aliment_"+ str(i)+" constraint"

aliment_A=[]
aliment_B=[]
aliment_C=[]
aliment_D=[]
aliment_E=[]
for i in range(len(m)):
    for j in range(len(m[i])):
        if j ==len(m[i])-1 and m[i][j]=='A':
            aliment_A.append(ls2[i])
        if j ==len(m[i])-1 and m[i][j]=='B':
            aliment_B.append(ls2[i])
        if j ==len(m[i])-1 and m[i][j]=='C':
            aliment_C.append(ls2[i])    
        if j ==len(m[i])-1 and m[i][j]=='D':
            aliment_D.append(ls2[i])    
        if j ==len(m[i])-1 and m[i][j]=='E':
            aliment_E.append(ls2[i])   
            
#print(aliment_A)            
#print(aliment_B)
#print(aliment_C)
#print(aliment_D)
#print(aliment_E)

for i in range(len(aliment_A)):
    for j in range(len(aliment_B)):
        prob1 += aliment_B[j]+ epsilon_0 <= aliment_A[i]
        
for i in range(len(aliment_B)):
    for j in range(len(aliment_C)):
        prob1 += aliment_C[j]+ epsilon_1 <= aliment_B[i]
        
for i in range(len(aliment_C)):
    for j in range(len(aliment_D)):
        prob1 += aliment_D[j]+ epsilon_2 <= aliment_C[i]

for i in range(len(aliment_D)):
    for j in range(len(aliment_E)):
        prob1 += aliment_E[j]+ epsilon_3 <= aliment_D[i]        
        
#print(prob1)
df4=df3['Énergie'].sort_values().index
df5=df3['Fibres'].sort_values().index
df6=df3['Protéines'].sort_values().index
df7=df3['Acides gras saturés'].sort_values().index
df8=df3['Sucre'].sort_values().index
df9=df3['Sodium'].sort_values().index

#print(df3['Acides gras saturés'].sort_values())
ls23=[]
#list des index des valeurs de la colonne énergie dans l'ordre décroissante
ls23=df4.values.tolist()

ls24=[]
ls24=df5.values.tolist()


ls25=[]
ls25=df6.values.tolist()

ls26 =[]
ls26=df7.values.tolist()

ls27=[]
ls27=df8.values.tolist()

ls28=[]
ls28=df9.values.tolist()
#print (ls28)

# Contraintes monotonie sur le critere 1 à minimiser 
lis1=df3['Énergie'].sort_values().tolist()     
for i in range(len(lis1)-1):
    if lis1[i]!=0.0 and lis1[i+1]!=0.0 and lis1[i]!=lis1[i+1]:
        prob1 += U_dict.get("list des utilité "+str(ls23[i+1]))[0] + ls1[i+4] <= U_dict.get("list des utilité "+str(ls23[i]))[0]

# Contraintes monotonie sur le critere 2 à maximiser 
lis2=df3['Fibres'].sort_values().tolist()     
for i in range(len(lis2)-1):
    if lis2[i]!=0.0 and lis2[i+1]!=0.0 and lis2[i]!=lis2[i+1]:
        prob1 += U_dict.get("list des utilité "+str(ls24[i]))[1] + ls1[i+4] <= U_dict.get("list des utilité "+str(ls24[i+1]))[1]


# Contraintes monotonie sur le critere 3 à maximiser
lis3=df3['Protéines'].sort_values().tolist()    
for i in range(len(lis3)-1):
    if lis3[i]!=0.0 and lis3[i+1]!=0.0 and lis3[i]!=lis3[i+1]:
        prob1 += U_dict.get("list des utilité "+str(ls25[i]))[2] + ls1[i+4] <= U_dict.get("list des utilité "+str(ls25[i+1]))[2]


# Contraintes monotonie sur le critere 4 à minimiser
lis4=df3['Acides gras saturés'].sort_values().tolist()      
for i in range(len(lis4)-1):
    if lis4[i]!=0.0 and lis4[i+1]!=0.0 and lis4[i]!=lis4[i+1]:
        prob1 += U_dict.get("list des utilité "+str(ls26[i+1]))[3] + ls1[i+4] <= U_dict.get("list des utilité "+str(ls26[i]))[3]

        
# Contraintes monotonie sur le critere 5 à minimiser         
lis5=df3['Sucre'].sort_values().tolist()     
for i in range(len(lis5)-1):
    if lis5[i]!=0.0 and lis5[i+1]!=0.0 and lis5[i]!=lis5[i+1]:
        prob1 += U_dict.get("list des utilité "+str(ls27[i+1]))[4] + ls1[i+4] <= U_dict.get("list des utilité "+str(ls27[i]))[4]        
        

# Contraintes monotonie sur le critere 6 à minimiser        
lis6=df3['Sodium'].sort_values().tolist()      
for i in range(len(lis6)-1):
    if lis6[i]!=0.0 and lis6[i+1]!=0.0 and lis6[i]!=lis6[i+1]:
        prob1 += U_dict.get("list des utilité "+str(ls28[i+1]))[5] + ls1[i+4] <= U_dict.get("list des utilité "+str(ls28[i]))[5]               
        
                
#print(prob1)   

# The problem data is written to an .lp file
prob1.writeLP("The Nutriscore_final_3.lp")

# The problem is solved using PuLP's choice of Solver
prob1.solve()

# The status of the solution is printed to the screen
print("Statut:", LpStatus[prob1.status])
# Output= 
# Status: Optimal

# Each of the variables is printed with it's resolved optimum value
for v in prob1.variables():
    print(v.name, "=", v.varValue)


# The optimised objective function value is printed to the screen
print("Valeur fonction objectif = ", value(prob1.objective))



# code pour afficher les résultats de PL dans un DataFrame
res2={}
for v in prob1.variables():
    if v.name.split('_')[0] == 'utilite':
        res2[v.name]=v.varValue

#list des aliments
lms=[]

for j in range(50):
    ls=[] 
    for k in range(1,7):
        ls.append(res2["utilite_"+str(k)+"_alim_"+str(j)]) 
    lms.append(ls)
#print(res2)    
#print(lms)    
dfm = pd.DataFrame(lms, columns =['Énergie', 'Fibres','Protéines','Acides gras saturés','Sucre','Sodium'])  
print(dfm ) 


