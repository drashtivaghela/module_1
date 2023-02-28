#!/usr/bin/env python
# coding: utf-8

import numpy as np
cric_data=np.loadtxt("cric.tsv",skiprows=1)

cric_data

Sachin=cric_data[:,1]
Dravid=cric_data[:,2]
India=cric_data[:,3]

def stats(x):
    a=np.mean(x)
    print("Mean:",a)
    b=np.median(x)
    print("Median:",b)

stats(Sachin)

stats(Dravid)

stats(India)
