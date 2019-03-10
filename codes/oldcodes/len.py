f=open('../train.ann','r')
fa=f.readlines()
maxn=0
for i in range(0,len(fa)-1):
    fp=fa[i-1].split(' ')
    ff=fa[i].split(' ')
    fn=fa[i+1].split(' ')
    if(ff[-1]=='I-PER\n' and fp[-1]!='I-PER\n'):
        print(ff[0])
        for j in range(i+1,len(fa)):
            fk=fa[j].split(' ')
            if(fk[-1]=='I-PER\n'):
                print(fk[0])
            else:
                if(maxn<j-i):
                    maxn=j-i
                print(j-i)
                break
print(maxn)
