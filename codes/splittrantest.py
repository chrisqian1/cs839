import random
name=open('../data/name.txt','r')
namel=name.readlines()
name.close
for names in namel:
    namels=namels.strip(' ''\n')
idt=random.sample(namel,100)
for i in range(0,len(namel)):
    f=open('../data/'+namel[i],'r')
    if(namel[i] in idt):
        g=open('../testing set J/'+namel[i],'w')
    else:
        g=open('../training set I/'+namel[i],'w')
    f1=f.readlines()
    g.writelines(f1)
    f.close
    g.close
