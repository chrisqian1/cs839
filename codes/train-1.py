import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer  
from sklearn.model_selection import cross_val_score,train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression,Lasso
from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
name1=open('../data-4-train/name.txt','r')
name1l=name1.readlines()
name1.close
name2=open('../data-4-test/name.txt','r')
name2l=name2.readlines()
name2.close
punc=[',','.','/',';','\'','[',']','\\','`','-','=','<','>','?',':','"','{','}','|','~','!','@','#','$','%','^','&','*','(',')','_','+','\n']
spepre=['secretary','secretaries','president','presidents','judge','judges','general','generals','gen.','executive','executives','prince','princes','princess','princesses','attorney','attorneies','dr.','mr.','mr','mrs.','mrs','diva','captain','captains','correspondent','correspondents','bishop','bishopes','lieutenant','lieutenants','chief','chiefes','official','officials','\'m','\'s','said','say','says','saying','spoke','sir','madam','husband','wife','chief','representative','king','queen','diplomat','detective','boss','minister','governor','leader','striker','manager','champion','analyst','spokesman','fighter','soldier','chief-of-staff','goalkeeper','defenders','strikers', 'vice-president','mayor','actor','rapist','prosecutor','defender','manager','keeper','semifinalist', 'secretary','chairman', 'director', 'monsignor','ambassador','head', 'neither','chancellor', 'publish','woman','champion','veteran','doctor','quoted', 'met','strategist','correspondent','predecessor','inspector','judge']
spepre2=['er','or']
spepre3=['man','men','ist','ian','ers','ors']
spepre4=['ists','ians']
spepre5=['woman','women']
spepre8=['year-old']
spesuf=['said','says','saying','spoke','tells','telling','told','hopes','hoped','announces','announced','claims','claimed','denied','denies','plans','planned','joins','joined','admitted','admits','convicts','convicted','vows','vowed','himself','herself','gives','gave','does','did','has','had','was','were','is','being','who','\'s','pardoned','pardon','explained','pulled','retired','took','takes', 'take','walked','walks','walk','dunked','dunk','dunks','drove','drive','driving','drives','allowed','allow','allows','scattered','scatter','scatters','put','believe','believes','believed','rushed','rush','threw','picked','walked','won','fired','shot','hit', 'added','goes','went','head', 'met','gives','gave','give','began','begins','begin','resigned','resign','joined','join','joins','overcame','overcomes','overcome','decided','decides','pitched','pitches','scored','scores', 'stand','stands','met','meet','meets','meeting','died','led','arrived','asked','asks','ask','flew','sitting','joked','joking','jokes','proposed','chief','clocked','received','shot','demonstrated','beat','drew','hired','leader','participated','ordered','opens','opened','open','faces','faced','facing','quoted','took','vows','shake','came','come','angered','lived','lives','reports','reported','signed','reiterated','iterated','iterate','reiterate','iterates','reiterates','left','returned','made','caught']
norm=open('../names/elp-voc-ab.txt','r')
normal=norm.readlines()
normdict={}
for t in normal:
    x=t.split(' ')
    normdict[x[0]]=1
male=open('../names/male.txt','r')
malename=male.readlines()
for malenames in malename:
    malenames=malenames.strip('\n')
male.close
female=open('../names/female.txt','r')
femalename=female.readlines()
for femalenames in femalename:
    femalenames=femalenames.strip('\n')
female.close
family=open('../names/family.txt','r')
familyname=family.readlines()
for familynames in familyname:
    familynames=familynames.strip('\n')
family.close
names=open('../names/names.txt','r')
namesn=names.readlines()
for namesni in namesn:
    namesni=namesni.strip('\n')
names.close
namesn.extend(malename)
namesn.extend(femalename)
namesn.extend(familyname)
namedict={}
for namesni in namesn:
    namedict[namesni]=1
names=['name']
result1=list()
result2=list()
for i in range(0,len(name1l)):
    print(i)
    fa=open('../data-4-train/'+str(name1l[i].strip()),'r')
    f1=fa.readlines()
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
                title=0
                if(k==0):
                    title=1
                prefix1=0
                prefix2=0
                suffix1=0 
                preupper=0
                prenum=0
                sufupper=0
                sufnum=0
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
                    if(ff[pre].lower() in spepre):
                        prefix1=1
                    if(ff[pre][-2:] in spepre2 or ff[pre][-3:] in spepre3 or ff[pre][-4:] in spepre4 or ff[pre][-5:] in spepre5 or ff[pre][-8:] in spepre8):
                        prefix2=1
                    if(ff[pre][0].isupper()):
                        preupper=1
                    for l in ff[pre]:
                        if (l.isdigit()):
                            prenum=1
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
                         suffix1=1
                    if(ff[suf][0].isupper()):
                        sufupper=1
                    for l in ff[suf]:
                        if(l.isdigit()):
                            sufnum=1                        
                re=ff[k:m+1]
                dic1=0
                dic2=0
                if(len(re)==1):
                    if(re[0].strip('<>''</>').title() in namedict):
                        dic1=1
                        dic2=1
                else:
                    if(re[0].strip('<>''</>').title() in namedict):
                        dic1=1
                    if(re[len(re)-1].strip('<>''</>''\n').title() in namedict or re[len(re)-2].strip('<>''</>''\n').title()+' '+re[len(re)-1].strip('<>''</>''\n').title() in namedict):
                        dic2=1
                normdic1=0
                normdic2=0
                norm1=0
                norm2=0
                for n in re:
                    if(n.lower() in normdict):
                        norm1+=1
                    else:
                        norm2+=1
                if(norm1>0):
                    normdic1=1
                if(norm2==0):
                    normdic2=1
                upper=0
                for n in range(0,len(re)):
                    re[n]=re[n].strip('<>''</>''\n')
                    if(re[n][0].isupper()==False):
                        upper+=1
                allupper=0
                if(' '.join(re).isupper() and '.' not in ' '.join(re)):
                    allupper=1
                if(upper==0 and allupper==0):
                    tag=0
                    for t in range(0,len(tag1)):
                        if( k >= tag1[t] and m <= tag2[t]):
                            tag=tag+1
                    if(tag>0):
                        tag=1
                    res=[' '.join(re)]
                    for n in range(0,len(re)):
                        if('name:'+re[n] not in names):
                            names.append('name:'+re[n])
                        res.append('name:'+re[n])
                    if(pre!=-1):
                        prefix=ff[pre].strip('<>''</>''\n').lower()
                        if('pre:'+prefix not in names):
                            names.append('pre:'+prefix)
                        res.append('pre:'+prefix)
                    if(suf!=-1):
                        suffix=ff[suf].strip('<>''</>''\n').lower()
                        if('suf:'+suffix not in names):
                            names.append('suf:'+suffix)
                        res.append('suf:'+suffix)
                    res.append(normdic1)
                    res.append(normdic2)
                    res.append(title)
                    res.append(prefix1)
                    res.append(prefix2)
                    res.append(suffix1)
                    res.append(preupper)
                    res.append(prenum)
                    res.append(sufupper)
                    res.append(sufnum)
                    res.append(dic1)
                    res.append(dic2)
                    res.append(tag)
                    result1.append(res)
for i in range(0,len(name2l)):
    print(i)
    fa=open('../data-4-test/'+str(name2l[i].strip()),'r')
    f1=fa.readlines()
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
                title=0
                if(k==0):
                    title=1
                prefix1=0
                prefix2=0
                suffix1=0   
                preupper=0
                prenum=0
                sufupper=0
                sufnum=0 
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
                    if(ff[pre].lower() in spepre):
                        prefix1=1
                    if(ff[pre][-2:] in spepre2 or ff[pre][-3:] in spepre3 or ff[pre][-4:] in spepre4 or ff[pre][-5:] in spepre5 or ff[pre][-8:] in spepre8):
                        prefix2=1
                    if(ff[pre][0].isupper()):
                        preupper=1
                    for l in ff[pre]:
                        if(l.isdigit()):
                            prenum=1
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
                        suffix1=1
                    if(ff[suf][0].isupper()):
                        sufupper=1
                    for l in ff[suf]:
                        if(l.isdigit()):
                            sufnum=1                        
                re=ff[k:m+1]
                re=ff[k:m+1]
                dic1=0
                dic2=0
                if(len(re)==1):
                    if(re[0].strip('<>''</>').title() in namedict):
                        dic1=1
                        dic2=1
                else:
                    if(re[0].strip('<>''</>').title() in namedict):
                        dic1=1
                    if(re[len(re)-1].strip('<>''</>''\n').title() in namedict or re[len(re)-2].strip('<>''</>''\n').title()+' '+re[len(re)-1].strip('<>''</>''\n').title() in namedict):
                        dic2=1
                normdic1=0
                normdic2=0
                norm1=0
                norm2=0
                for n in re:
                    if(n.lower() in normdict):
                        norm1+=1
                    else:
                        norm2+=1
                if(norm1>0):
                    normdic1=1
                if(norm2==0):
                    normdic2=1
                upper=0
                for n in range(0,len(re)):
                    re[n]=re[n].strip('<>''</>''\n')
                    if(re[n][0].isupper()==False):
                        upper+=1
                allupper=0
                if(' '.join(re).isupper() and '.' not in ' '.join(re)):
                    allupper=1
                if(upper==0 and allupper==0):
                    tag=0
                    for t in range(0,len(tag1)):
                        if( k >= tag1[t] and m <= tag2[t]):
                            tag=tag+1
                    if(tag>0):
                        tag=1
                    res=[' '.join(re)]
                    for n in range(0,len(re)):
                        if('name:'+re[n] not in names):
                            names.append('name:'+re[n])
                        res.append('name:'+re[n])
                    if(pre!=-1):
                        prefix=ff[pre].strip('<>''</>''\n').lower()
                        if('pre:'+prefix not in names):
                            names.append('pre:'+prefix)
                        res.append('pre:'+prefix)
                    if(suf!=-1):
                        suffix=ff[suf].strip('<>''</>''\n').lower()
                        if('suf:'+suffix not in names):
                            names.append('suf:'+suffix)
                        res.append('suf:'+suffix)
                    res.append(normdic1)
                    res.append(normdic2)
                    res.append(title)
                    res.append(prefix1)
                    res.append(prefix2)
                    res.append(suffix1)
                    res.append(preupper)
                    res.append(prenum)
                    res.append(sufupper)
                    res.append(sufnum)
                    res.append(dic1)
                    res.append(dic2)
                    res.append(tag)
                    result2.append(res)
names.append('normdic1')
names.append('normdic2')
names.append('title')
names.append('prefix1')
names.append('prefix2')
names.append('suffix1')
names.append('preupper')
names.append('prenum')
names.append('sufupper')
names.append('sufnum')
names.append('dic1')
names.append('dic2')
names.append('tag')
data1={}
for i in range(0,len(names)-13):
    data1[names[i]]=list()
    for j in range(0,len(result1)):
        if(names[i] in result1[j]):
            data1[names[i]].append(1)
        else:
            data1[names[i]].append(0)
data1['name']=list()
data1['normdic1']=list()
data1['normdic2']=list()
data1['title']=list()
data1['prefix1']=list()
data1['prefix2']=list()
data1['suffix1']=list()
data1['preupper']=list()
data1['prenum']=list()
data1['sufupper']=list()
data1['sufnum']=list()
data1['dic1']=list()
data1['dic2']=list()
data1['tag']=list()
for j in range(0,len(result1)):
    data1['name'].append(result1[j][0])
    data1['normdic1'].append(result1[j][-13])
    data1['normdic2'].append(result1[j][-12])
    data1['title'].append(result1[j][-11])
    data1['prefix1'].append(result1[j][-10])
    data1['prefix2'].append(result1[j][-9])
    data1['suffix1'].append(result1[j][-8])
    data1['preupper'].append(result1[j][-7])
    data1['prenum'].append(result1[j][-6])
    data1['sufupper'].append(result1[j][-5])
    data1['sufnum'].append(result1[j][-4])
    data1['dic1'].append(result1[j][-3])
    data1['dic2'].append(result1[j][-2])
    data1['tag'].append(result1[j][-1])
datatrain=pd.DataFrame(data1)
datatrain.to_csv('data-train.csv') 
data2={}
for i in range(0,len(names)-13):
    data2[names[i]]=list()
    for j in range(0,len(result2)):
        if(names[i] in result2[j]):
            data2[names[i]].append(1)
        else:
            data2[names[i]].append(0)
data2['name']=list()
data2['normdic1']=list()
data2['normdic2']=list()
data2['title']=list()
data2['prefix1']=list()
data2['prefix2']=list()
data2['suffix1']=list()
data2['preupper']=list()
data2['prenum']=list()
data2['sufupper']=list()
data2['sufnum']=list()
data2['dic1']=list()
data2['dic2']=list()
data2['tag']=list()
for j in range(0,len(result2)):
    data2['name'].append(result2[j][0])
    data2['normdic1'].append(result2[j][-13])
    data2['normdic2'].append(result2[j][-12])
    data2['title'].append(result2[j][-11])
    data2['prefix1'].append(result2[j][-10])
    data2['prefix2'].append(result2[j][-9])
    data2['suffix1'].append(result2[j][-8])
    data2['preupper'].append(result2[j][-7])
    data2['prenum'].append(result2[j][-6])
    data2['sufupper'].append(result2[j][-5])
    data2['sufnum'].append(result2[j][-4])
    data2['dic1'].append(result2[j][-3])
    data2['dic2'].append(result2[j][-2])
    data2['tag'].append(result2[j][-1])
datatest=pd.DataFrame(data2)
print(datatest)
datatest.to_csv('data-test.csv') 
