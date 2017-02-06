#    Copyright 2008 Ealdwulf Wuffinga

#    This file is part of BBChop.
#
#    BBChop is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    BBChop is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with BBChop.  If not, see <http://www.gnu.org/licenses/>.
import BBChop
import random
import pdb
import copy
import sys
import math

Ntests=100000
N=4
prior=[ 1.0/N for i in range(N+1)]
tcounts=[4,5,6,7]

occ={}
for i in range(Ntests):
    prob=random.random()
    loc=random.randint(0,N-1)

    counts=[]
    for j in range(N):
        t=0
        d=0
        for k in range(tcounts[j]):
           if j>=loc and random.random()<prob:
               d=d+1
           else:
               t=t+1
        counts.append((t,d))
    counts.append((0,0))
    cInd=(counts[0],counts[1],counts[2],counts[3],counts[4])
    if cInd not in occ:
        occ[cInd]=[0 for i in range(N+1)]
    occ[cInd][loc]=occ[cInd][loc]+1

    if(i%10000==9999):
        sys.stderr.write("%d\n" % (i+1))

def lo(x):
    if((1-float(x))==0):
        return "OO"
    if(float(x)==0):
        return "-OO"
    return math.log(float(x)/(1-float(x)))
for (counts,olist) in occ.items():
    
    (locProbs,findProbs)=BBChop.probs(counts,prior)
    print("c",counts)
#    pdb.set_trace()
    print("l",list(map(lo,locProbs)))
    sp=[(float(i)/sum(olist)) for i in olist]
    print("s",sum(olist),list(map(lo,sp)))
    


    
