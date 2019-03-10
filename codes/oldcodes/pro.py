import random
idt=random.sample(range(1,947),300)
print(idt)
count=0
for i in range(1,947):
    print(i)
    fa=open('../data-4/data-'+str(i)+'.txt','r')
    f1=fa.readlines()
    
    fa.close
    if(i in idt):
        ft=open('../data-4-1/data-'+str(i)+'.txt','w')
        ft.writelines(f1)
        ft.close
        for j in range(0,len(f1)):
            ff=f1[j].split(' ')
            for k in range(0,len(ff)):
                if('<>' in ff[k]):
                    count+=1
    k=0
    for j in range(0,(len(f1))):
        if(f1[j].find('PER|null|SPC|NAM')!=-1):
            k+=1
            print(f1[j])
            ff=f1[j].split(' ')
            f3=f2[int(ff[-5])].split(' ')
            f3[int(ff[-4])]='<>'+f3[int(ff[-4])]
            f3[int(ff[-3])]=f3[int(ff[-3])]+'</>'
            f2[int(ff[-5])]=' '.join(f3)
    fw=open('../data-4-l/'+namel[i]+'.txt','w')   
    num.append(namel[i]+','+str(k)+'\n')    
    fw.writelines(f2)
    fw.close
    ft.close
    fa.close
fn=open('../data-4-l/number.txt','w')
fn.writelines(num)
fn.close
