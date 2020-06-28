from time import*
from tKnapsack import*
from dKnapsack import*
from bKnapsack import*
from bbKnapsack import*

import matplotlib.pyplot as plt
import matplotlib as mpl

iter = 100

beginTime = time()
for i in range(iter):
    TraverRun()
endTime = time()
runTime1 = (endTime - beginTime)/iter

beginTime = time()
for i in range(iter):
    mainRun(type = 'right2left')
endTime = time()
runTime21 = (endTime - beginTime)/iter

beginTime = time()
for i in range(iter):
    mainRun(type = 'left2rightt')
endTime = time()
runTime22 = (endTime - beginTime)/iter

beginTime = time()
for i in range(iter):
    BacktrackRun()
endTime = time()
runTime3 = (endTime - beginTime)/iter

beginTime = time()
for i in range(iter):
    BranchBoundRun()
endTime = time()
runTime4 = (endTime - beginTime)/iter

'''
mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

x = [1,2,3,4,5]
y = [runTime1,runTime21,runTime22,runTime3,runTime1]
plt.bar(x, y, align="center", color="c",tick_label=["Traversal method", "Dynamic program(R2L)", "Dynamic program(L2R)", "Backtrack", "Branch and bound"], hatch="/")
plt.xlabel("Algorithm")
plt.ylabel("Run time")
plt.show()
'''

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

x = [1,2,3,4,5]
y = [512,0,0,1,16]
plt.bar(x, y, align="center", color="c",tick_label=["Traversal method", "Dynamic program(R2L)", "Dynamic program(L2R)", "Backtrack", "Branch and bound"], hatch="/")
plt.xlabel("Algorithm")
plt.ylabel("Number of accessing leaf nodes")
plt.show()
