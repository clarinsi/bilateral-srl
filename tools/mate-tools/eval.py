#!/usr/bin/python
import sys
sents=0
predicate_true=[]
predicate_pred=[]
args_true=[]
args_pred=[]
for gold,pred in zip(open(sys.argv[1]),open(sys.argv[2])):
  if gold.strip()=='':
    sents+=1
  else:
    true=gold.strip().split('\t')
    pred=pred.strip().split('\t')
    predicate_true.append(true[12])
    predicate_pred.append(pred[12])
    min_len=min([len(pred),len(true)])
    for t,p in zip(true[14:min_len]+['_']*(len(true)-min_len),pred[14:min_len]+['_']*(len(pred)-min_len)):
      if t!='_' or p!='_':
        args_true.append(t)
        args_pred.append(p)
from sklearn.metrics import classification_report,f1_score,confusion_matrix
print classification_report(predicate_true,predicate_pred)
print classification_report(args_true,args_pred)
print f1_score(args_true,args_pred,average='macro')
print confusion_matrix(args_true,args_pred)