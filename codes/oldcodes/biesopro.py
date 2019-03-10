doc=open('../train.ann','r')
data=doc.readlines()
i=1
result=['']
w=open('../data-4-1/data-1.txt','w')
num=list()
count=0
for j in range(1,(len(data)-1)):
    print(j)
    fp=data[j-1].split(' ')
    ff=data[j].split(' ')
    fn=data[j+1].split(' ')
    if(ff[0]=='-DOCSTART-'):
        num.append('data-'+str(i)+','+str(count)+'\n')
        count=0
        w.writelines(result)
        w.close
        i+=1
        w=open('../data-4-1/data-'+str(i)+'.txt','w')
        print(result)
        result=['']
    elif(data[j]!='\n'):
        if(ff[-1]=='I-PER\n' and fp[-1]!='I-PER\n'):
            result[-1]=result[-1]+' <>'+ff[0]
            count+=1
            if(fn[-1]!='I-PER\n'):
                result[-1]=result[-1]+'</>'
        elif(ff[-1]=='B-PER\n' and fp[-1]!='B-PER\n'):
            result[-1]=result[-1]+' <>'+ff[0]
            count+=1
            if(fn[-1]!='B-PER\n'):
                result[-1]=result[-1]+'</>'
        elif(ff[-1]=='I-PER\n' and fn[-1]!='I-PER\n'):
            result[-1]=result[-1]+' '+ff[0]+'</>'
        elif(ff[-1]=='B-PER\n' and fn[-1]!='B-PER\n'):
            result[-1]=result[-1]+' '+ff[0]+'</>'
        else:
            result[-1]=result[-1]+' '+ff[0]
    elif(fp[0]!='-DOCSTART-'):   
        result[-1]=result[-1]+data[j]
        result[-1]=result[-1].lstrip(' ')
        result.append('')
ff=data[j+1].split(' ')
result[-1]=result[-1]+' '+ff[0]+'\n'
result[-1]=result[-1].lstrip(' ')
num.append('data-'+str(i)+','+str(count)+'\n')
no=open('../data-4-1/number.txt','w')
no.writelines(num)
no.close
print(result)
w.writelines(result)
w.close
doc.close
