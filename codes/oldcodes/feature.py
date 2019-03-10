import numpy as np
import pandas as pd
name=open('../data-4-2/name.txt','r')
namel=name.readlines()
name.close
punc=[',','.','/',';','\'','[',']','\\','`','-','=','<','>','?',':','"','{','}','|','~','!','@','#','$','%','^','&','*','(',')','_','+','\n']
digit=['0','1','2','3','4','5','6','7','8','9']
spepre=['secretary','secretaries','president','presidents','judge','judges','general','generals','gen.','executive','executives','prince','princes','princess','princesses','attorney','attorneies','dr.','mr.','mr','mrs.','mrs','diva','captain','captains','correspondent','correspondents','bishop','bishopes','lieutenant','lieutenants','chief','chiefes','official','officials','\'m','\'s','said','say','says','saying','spoke','sir','madam','husband','wife','chief','representative','king','queen','diplomat','detective','boss']
spepre2=['er','or']
spepre3=['man','men','ist','ian','ers','ors']
spepre4=['ists','ians']
spepre5=['woman','women']
spepre8=['year-old']
spesuf=['said','says','saying','spoke','tells','telling','told','hopes','hoped','announces','announced','claims','claimed','denied','denies','plans','planned','joins','joined','admitted','admits','convicts','convicted','vows','vowed','himself','herself','gives','gave','does','did','has','had','was','were','is','being','who','\'s','pardoned','pardon']
male=open('../names/male.txt','r')
malename=male.readlines()
for i in range(0,len(malename)):
    malename[i]=malename[i].strip('\n')
male.close
female=open('../names/female.txt','r')
femalename=female.readlines()
for i in range(0,len(femalename)):
    femalename[i]=femalename[i].strip('\n')
female.close
family=open('../names/family.txt','r')
familyname=family.readlines()
for i in range(0,len(familyname)):
    familyname[i]=familyname[i].strip('\n')
family.close
names=open('../names/names.txt','r')
namesn=names.readlines()
for i in range(0,len(namesn)):
    namesn[i]=namesn[i].strip('\n')
names.close
namesn.extend(malename)
namesn.extend(femalename)
namesn.extend(familyname)
# ~ t=0
# ~ for i in range(0,len(namel)):
    # ~ count=0
    # ~ fa=open('../data-4-2/'+str(namel[i].strip()),'r')
    # ~ f1=fa.readlines()
    # ~ for j in range(0,len(f1)):
        # ~ if('#' in f1[j]):
            # ~ count+=1
    # ~ print(count)
    # ~ t=t+count
# ~ print(t)
for i in range(0,len(namel)):
    print(i)
    fa=open('../data-4-2/'+str(namel[i].strip()),'r')
    f1=fa.readlines()
    result=['name#number#prefix#suffix#firstname#lastname#y\n']
    for j in range(0,len(f1)):
        ff=f1[j].split(' ')
        tag1=[-1]
        tag2=[-1]
        for k in range(0,len(ff)):
            if('<>' in ff[k]):
                tag1.append(k)
            if('</>' in ff[k]):
                tag2.append(k)
        for k in range(0,len(ff)):
            for m in range(k,min(k+6,len(ff))):
                count=0
                for n in range(0,len(ff[m])):
                    if(ff[m][n] not in punc):
                        count+=1
                if(count==0):
                    break
                prefix=0
                pre=-1
                count=0
                if(k!=0):
                    for cha in range(0,len(ff[k-1])):
                        if(ff[k-1][cha] not in punc):
                            count+=1
                    if(count==0):
                        if(k!=1):
                            count1=0
                            for cha in range(0,len(ff[k-2])):
                                if(ff[k-2][cha] not in punc):
                                    count1+=1
                            if(count1==0):
                                if(k!=2):
                                    pre=k-3
                                else:
                                    pre=-1
                            else:
                                pre=k-2
                        else:
                            pre=-1
                    else:
                        pre=k-1
                if(pre!=-1):
                     if(ff[pre].lower() in spepre or ff[pre][-2:] in spepre2 or ff[pre][-3:] in spepre3 or ff[pre][-4:] in spepre4 or ff[pre][-5:] in spepre5 or ff[pre][-8:] in spepre8):
                         prefix=1
                suffix=0
                suf=-1
                count=0
                if(m!=len(ff)-1):
                    for cha in range(0,len(ff[m+1])):
                        if(ff[m+1][cha] not in punc):
                            count+=1
                    if(count==0):
                        if(m!=len(ff)-2):
                            count1=0
                            for cha in range(0,len(ff[m+2])):
                                if(ff[m+2][cha] not in punc):
                                    count1+=1
                            if(count1==0):
                                if(m!=len(ff)-3):
                                    suf=m+3
                                else:
                                    suf=-1
                            else:
                                suf=m+2
                        else:
                            suf=-1
                    else:
                        suf=m+1
                if(suf!=-1):
                     if(ff[suf].lower() in spesuf):
                         suffix=1
                re=ff[k:m+1]
                tag=0
                for t in range(0,len(tag1)):
                    if( k >= tag1[t] and m <= tag2[t]):
                        tag=tag+1
                if(tag>0):
                    tag=1
                count=0
                for n in range(0,len(re)):
                    for o in range(0,len(re[n])):
                        if(re[n][o] in digit):
                            count+=1
                upper=0
                for n in range(0,len(re)):
                    if(re[n][0:2]=='<>' and re[n][2].isupper()==False):
                        upper+=1
                    elif(re[n][0:2]!='<>' and re[n][0].isupper()==False):
                        upper+=1
                if(upper>0):
                    upper=1
                dic1=0
                dic2=0
                if(len(re)==1):
                    if(re[0].strip('<>''</>').title() in namesn):
                        dic1=1
                        dic2=1
                else:
                    if(re[0].strip('<>''</>').title() in namesn):
                        dic1=1
                    if(re[len(re)-1].strip('<>''</>''\n').title() in namesn or re[len(re)-2].strip('<>''</>''\n').title()+' '+re[len(re)-1].strip('<>''</>''\n').title() in namesn):
                        dic2=1
                for n in range(0,len(re)):
                    if('</>\n' in re[n]):
                        re[n]=re[n].strip('</>\n')+'\n'
                    elif('</>' in re[n]):
                        re[n]=re[n].strip('</>')
                    if('<>' in re[n]):
                        re[n]=re[n].strip('<>')
                if(upper==0):
                    if(' '.join(re)[-1:]!='\n'):
                        result.append(' '.join(re)+'#'+str(m-k+1)+'#'+str(prefix)+'#'+str(suffix)+'#'+str(dic1)+'#'+str(dic2)+'#'+str(tag)+'\n')
                    else:
                        result.append(' '.join(re)[:-1]+'#'+str(m-k+1)+'#'+str(prefix)+'#'+str(suffix)+'#'+str(dic1)+'#'+str(dic2)+'#'+str(tag)+'\n')
    fr=open('../data-split-2/result-'+str(namel[i].strip()),'w')
    fr.writelines(result)
    fr.close
    fa.close
