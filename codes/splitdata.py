import random
name=open('../alldata/name.txt','r')
namel=name.readlines()
name.close
for names in namel:
    namels=namels.strip(' ''\n')
idt=random.sample(namel,300)
print(idt)
name=list()
for names in namel:
    if names in idt:
        f=open('../alldata'+names,'r')
        g=open('../data'+names,'r')
        f1=f.readlines()
        g.writelines()
        f.close
        g.close
