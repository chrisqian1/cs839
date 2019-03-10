ftestn=open('../data-4-test/name.txt','r')
testname=ftestn.readlines()
ftestn.close
testcount=0
for tests in testname:
    ftest=open('../data-4-test/'+tests.strip(' \n'),'r')
    test=ftest.readlines()
    ftest.close
    for lines in test:
        words=lines.split(' ')
        for word in words:
            if('<>' in word):
                testcount+=1
print(testcount)
ftrainn=open('../data-4-train/name.txt','r')
trainname=ftrainn.readlines()
ftrainn.close
traincount=0
for trains in trainname:
    ftrain=open('../data-4-train/'+trains.strip(' \n'),'r')
    train=ftrain.readlines()
    ftrain.close
    for lines in train:
        words=lines.split(' ')
        for word in words:
            if('<>' in word):
                traincount+=1
print(traincount)
