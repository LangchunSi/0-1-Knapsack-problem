# Backtrack method

'''
Define global class for storing global parameter
'''
class Global:
    '''
    n:        number of items
    capacity: capacity of bag
    value:    value of each item
    weight:   weight of each item
    currentW: current weight of bag
    currentV: current value of bag
    bestP:    current global best solution
    perV:     value of per weight
    order:    order of each item
    select:   selcction result
    '''
    capacity = 0
    value = []
    weight = []
    currentW = 0
    currentV = 0
    bestP = 0
    perV = []
    order = []
    select = []
    Final = []
    count = 0
    def __init__(self,c,v,w):
        # Initialization
        self.capacity = c
        self.value = v
        self.weight = w
        self.n = len(self.value)
        try:
            self.n == len(self.weight)
        except ValueError:
            print("Please check the number of weights and values")
        self.order = list(range(0,self.n))
        self.Final = self.select = [0]*self.n
        self.perV = [0.0]*self.n

        # sort
        for i in range(self.n):
            self.perV[i] = self.value[i]/self.weight[i]
        for i in range(0,self.n-1):
            for j in range(i+1,self.n):
                if self.perV[i] < self.perV[j]:
                    tempP = self.perV[i]
                    self.perV[i] = self.perV[j]
                    self.perV[j] = tempP

                    tempO = self.order[i]
                    self.order[i] = self.order[j]
                    self.order[j] = tempO

                    tempV = self.value[i]
                    self.value[i] = self.value[j]
                    self.value[j] = tempV

                    tempW = self.weight[i]
                    self.weight[i] = self.weight[j]
                    self.weight[j] = tempW

def Backtrack(i,GP):
    if i >= GP.n:
        GP.count += 1
        GP.bestP = GP.currentV
        GP.Final = GP.select[:] 
        return
    if GP.currentW + GP.weight[i] <= GP.capacity:
        GP.currentW += GP.weight[i]
        GP.currentV += GP.value[i]
        GP.select[i] = 1
        Backtrack(i+1,GP)
        GP.currentW -= GP.weight[i]
        GP.currentV -= GP.value[i]
    if Bound(i+1,GP) > GP.bestP:
        Backtrack(i+1,GP)

def Bound(i,GP):
    cleft = GP.capacity - GP.currentW
    b = GP.currentV
    while i < GP.n and GP.weight[i] <= cleft:
        cleft -= GP.weight[i]
        b += GP.value[i]
        i += 1
    if i < GP.n:
        b += GP.perV[i]*cleft
    return b

def BacktrackRun(weight = [6,5,4,1,2,3,9,8,7],value = [1,2,3,7,8,9,6,5,4],capacity = 20):
    GP = Global(capacity,value,weight)
    Backtrack(0,GP)
    trueSelect = [0]*GP.n
    for i in range(0,GP.n):
        if GP.Final[i] != 0:
            trueSelect[GP.order[i]] = 1
    '''
    print("Number of accessing leaf nodes: ",GP.count)
    print("Select = ",trueSelect)
    print("Maximum value = ",GP.bestP)
    '''

if __name__ == '__main__':
    BacktrackRun()
    
