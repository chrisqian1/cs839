name=open('../data-result-1/name.txt','r')
namel=name.readlines()
name.close
pre=list()
pren=list()
suf=list()
sufn=list()
for i in range(0,len(namel)):
    fa=open('../data-result-1/'+str(namel[i].strip()),'r')
    f1=fa.readlines()
    fa.close
    for j in range(0,len(f1)):
        ff=f1[j].split(' ')
        for k in range(0,len(ff)):
            if('<>' in ff[k] and k!=0):
                if(ff[k-1] not in pre):
                    pre.append(ff[k-1])
                    pren.append(1)
                    print(pre)
                else:
                    pren[pre.index(ff[k-1])]=pren[pre.index(ff[k-1])]+1
            elif('</>' in ff[k] and k!=len(ff)-1):
                if(ff[k+1] not in suf):
                    suf.append(ff[k+1])
                    sufn.append(1)
                    print(pre)
                else:
                    sufn[suf.index(ff[k+1])]=sufn[suf.index(ff[k+1])]+1
pref=open('../data-result-1/pre.txt','w')
for i in range(0,len(pre)):
    pref.write(str(pre[i])+','+str(pren[i])+'\n')
pref.close
suff=open('../data-result-1/suf.txt','w')
for i in range(0,len(suf)):
    suff.write(str(suf[i])+','+str(sufn[i])+'\n')
suff.close
print(pre)
print(pren)
print(suf)
print(sufn)

