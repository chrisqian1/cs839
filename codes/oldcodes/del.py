import numpy as np
import pandas as pd
data = pd.read_csv("../data-2-1/data-2/number.txt")
for i in range(0,len(data)):
    fa=open('../data-2-1/data-2/'+str(data.iloc[i,0])+'-'+str(data.iloc[i,1])+'.txt','r')
    ft=open('../data-2-result/'+str(data.iloc[i,0])+'.txt','w')
    f1=fa.readlines()
    count=0
    for j in range(0,len(f1)):
        if(f1[j].find('</>')!=-1):
            ff=f1[j].split(' ')
            for k in range(0,len(ff)):
                if(ff[k].find('</>')!=-1):
                    count+=1
                    if(count % 2 == 1):
                        ff[k]='<>'+ff[k].lstrip('</>')
                        if(ff[k][-3:]=='</>'):
                            count+=1
            f1[j]=' '.join(ff)
            print(f1[j])
    ft.writelines(f1)
    ft.close
    fa.close

