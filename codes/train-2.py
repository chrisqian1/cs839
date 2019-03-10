import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer  
from sklearn.model_selection import cross_val_score,train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression,Lasso,PassiveAggressiveClassifier,SGDClassifier
from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB,ComplementNB,BernoulliNB
data=pd.read_csv('data-train.csv')
del data[list(data)[0]]
X_train=data.iloc[:,1:-1]
y_train=data.iloc[:,-1]
test=pd.read_csv('data-test.csv')
del test[list(test)[0]]
X_test=test.iloc[:,1:-1]
y_test=test.iloc[:,-1]
ac=0
re=0
count=0
fp=list()
fn=list()
for i in range(0,30):
    model=PassiveAggressiveClassifier(class_weight={0:3,1:1})
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test)
    # ~ model2=SGD()
    # ~ model2.fit(X_train,y_train)
    # ~ y_pred2=model2.predict_proba(X_test)
    # ~ y_pred=list()
    # ~ for j in range(0,len(y_pred1)):
        # ~ if(y_pred1[j][0]+y_pred2[j][0]>=1):
            # ~ y_pred.append(0)
        # ~ else:
            # ~ y_pred.append(1)
    acn=0
    aci=0
    ren=0
    rei=0 
    for j in range(0,len(X_test)):
        if(y_pred[j]>=0.5):
            acn+=1
            if(y_test.iloc[j]==1):
                aci+=1
            # ~ else:
                # ~ fp1=test.iloc[j,0]
                # ~ for k in range(len(list(X_test))-6):
                    # ~ if (X_test.iloc[j,k]==1 and 'name' not in list(X_test)[k]):
                        # ~ fp1=fp1+'#'+list(X_test)[k]
                # ~ fp1=fp1+'\n'
                # ~ fp.append(fp1)
        if(y_test.iloc[j]==1):
            ren+=1
            if(y_pred[j]>=0.5):
                rei+=1
            # ~ else:
                # ~ fn1=test.iloc[j,0]
                # ~ for k in range(len(list(X_test))-6):
                    # ~ if (X_test.iloc[j,k]==1 and 'name' not in list(X_test)[k]):
                        # ~ fn1=fn1+'#'+list(X_test)[k]
                # ~ fn1=fn1+'\n'
                # ~ fn.append(fn1)
    if(aci/acn>=0.9 and rei/ren>=0.6):
        count+=1
    print(aci/acn)
    print(rei/ren)
# ~ fpf=open('fp.txt','w')
# ~ fpf.writelines(fp)
# ~ fpf.close
# ~ fnf=open('fn.txt','w')
# ~ fnf.writelines(fn)
# ~ fnf.close
    # ~ ac=ac+aci/acn
    # ~ re=re+rei/ren
print(ac/30)
print(re/30)
print(count)
print(2*ac/30*re/30/(ac/30+re/30))
winsound.Beep(150,1000)
