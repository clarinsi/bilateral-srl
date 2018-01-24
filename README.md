# bilateral-srl

## Data

The data used for benchmarking various SRL tools was produced during the Croatian-Slovene bilateral project (Institute of Language and Linguistics, Zagreb, Jožef Stefan Institute, Ljubljana, further details to be added). The Croatian and Slovene datasets, which are parts of standard training corpora for Croatian (hr500k) and Slovene (ssj500k) are available in ```data/sl``` and ```data/hr``. For now, each dataset is split in training:testing data only (dev to be added when will become necessary), following a 8:2 ratio.

## mate-tools

We performed no adaptation of the tool, using German feature functions. The output on the tool is available in ```tools/mate-tools/hr.test.mate.out``` and ```tools/mate-tools/sl.test.mate.out```. The gold data is available in ```tools/mate-tools/hr.test.mate``` and ```tools/mate-tools/sl.test.mate```.

Evaluation is performed on (1) predicate identification and (2) semantic roles. While evaluating semantic roles, both the predicate and the label have to be correct to assess the instance as correct.

Important notice: features exploit lower levels of linguistic annotation which are currently manual / gold. Substituting these annotations with automatic ones is a to-do.

For evaluation the ```tools/mate-tools/eval.py``` script is used.

Croatian evaluation of (1) predicate identification and (2) semantic role label.

```
             precision    recall  f1-score   support

          Y       1.00      1.00      1.00      2021
          _       1.00      1.00      1.00     14614

avg / total       1.00      1.00      1.00     16635


             precision    recall  f1-score   support

       ACMP       0.82      0.78      0.80        23
        ACT       0.88      0.94      0.91       962
        AIM       0.56      0.40      0.47        45
      CAUSE       0.25      0.09      0.14        53
       COND       0.57      0.62      0.59        13
      CONTR       0.40      0.14      0.21        14
        DUR       0.59      0.38      0.46        88
      EVENT       0.83      0.58      0.68        26
       FREQ       1.00      0.33      0.50        15
       GOAL       0.52      0.30      0.38        43
        LOC       0.48      0.67      0.56        97
       MANN       0.42      0.48      0.45       100
      MEANS       0.38      0.52      0.44        21
      MODAL       0.92      0.97      0.94       115
     MWPRED       0.85      0.63      0.72        35
       ORIG       0.81      0.55      0.65        64
        PAT       0.82      0.81      0.81      1052
      PHRAS       0.17      0.08      0.11        12
      QUANT       0.85      0.40      0.54        43
        REC       0.80      0.75      0.78       117
        REG       0.52      0.36      0.43        47
      RESLT       0.84      0.82      0.83       562
      RESTR       0.00      0.00      0.00         7
     SOURCE       0.67      0.18      0.29        11
       TIME       0.58      0.73      0.65       238

avg / total       0.72      0.72      0.72      4062
```

Slovene evaluation of (1) predicate identification and (2) semantic role label.

```
             precision    recall  f1-score   support

          Y       1.00      1.00      1.00      2203
          _       1.00      1.00      1.00     18199

avg / total       1.00      1.00      1.00     20402


             precision    recall  f1-score   support

       ACMP       0.20      0.05      0.08        21
        ACT       0.94      0.95      0.94       972
        AIM       0.29      0.15      0.20        26
      CAUSE       0.43      0.30      0.35        71
       COND       0.53      0.40      0.46        60
      CONTR       0.40      0.09      0.14        23
        DUR       0.57      0.44      0.50        72
      EVENT       0.33      0.25      0.29        12
       FREQ       0.80      0.47      0.59        43
       GOAL       0.42      0.70      0.53        80
        LOC       0.50      0.72      0.59       233
       MANN       0.76      0.77      0.76       286
      MEANS       0.57      0.74      0.64        34
      MODAL       0.95      0.86      0.90       103
     MWPRED       0.90      0.92      0.91        66
       ORIG       0.48      0.16      0.24        63
        PAT       0.86      0.89      0.88      1021
      PHRAS       0.60      0.21      0.31        43
      QUANT       0.81      0.50      0.62        52
        REC       0.77      0.72      0.74       205
        REG       0.39      0.29      0.34        92
      RESLT       0.90      0.73      0.80       530
      RESTR       0.00      0.00      0.00         1
     SOURCE       0.33      0.42      0.37        24
       TIME       0.52      0.77      0.62       287

avg / total       0.77      0.76      0.75      4462
```

More tools / improvements to follow! Please contact nljubesi AT gmail.com if you want to have a go at the problem! This is a community effort!
