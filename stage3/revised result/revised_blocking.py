def Jaccard(a,b):
    a='##'+a+'##'
    b='##'+b+'##'
    Ca=[]
    Cb=[]
    for j in range(0,len(a)-2):
        Ca.append(a[j:j+3])
    for j in range(0,len(b)-2):
        Cb.append(b[j:j+3])
    o=0
    for j in Ca:
        if j in Cb:
            o+=1
    return o/(len(a)+len(b)-o)
    
    
import numpy as np
import pandas as pd
sephora=pd.read_csv('sephora')
ulta=pd.read_csv('ulta')
candidate=pd.read_csv('cosmestics_apply_rules_ds')
print(len(candidate))
t=[]
for i in range(0,len(candidate)):
    flag=0
    a=sephora.iloc[candidate.iloc[i,0],2].upper().split(' ')
    b=ulta.iloc[candidate.iloc[i,1],2].upper().split(' ')
    o=0
    for j in a:
        if j in b:
            o+=1
    if o/(len(a)+len(b)-o)<0.5:
        flag+=1
    else:
        a=sephora.iloc[candidate.iloc[i,0],1].upper()
        b=ulta.iloc[candidate.iloc[i,1],1].upper()
        if Jaccard(a,b)<0.3:
            flag+=1
    if flag==1:
        t.append(i)
candidate.drop(t,inplace=True)
print(len(candidate))
candidate.to_csv('candidate_blocking.csv',sep=',',header=True,index=False)

# ~ import random
# ~ candidate=pd.read_csv('candidate_blocking.csv')
# ~ idt=random.sample(range(0,len(candidate)),len(candidate)-400)
# ~ candidate.drop(idt,inplace=True)
# ~ candidate.to_csv('candidate_select_400.csv',sep=',',header=True,index=False)

