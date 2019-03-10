This directory contains all the codes we write during the program.
Codes in the 'oldcodes' directory is those we try during the project ( e.g. try different dataset or different method or different features) but failed.
Codes directly under the 'codes' directory are the codes we use for the final result.
splitdata.py randomly choose 300 documents for us to use.
splittrantest.py split 300 documents in to training set I(200) and testing set J(100)
feature.py convert set I and set J into matrix with features and tags.
train-1.py contains results after we performing cross validation on set I.
train-2.py contains results before rule-based post-processing.
