# Traversal method

# Define global parameter
class Global:
    '''
    n:        number of items
    value:    value of each item
    weight:   weight of each item
    capacity: capacity of bag
    currentW: current weight
    currentV: current value
    select:   current selection of items
    bestS:    current best selection
    bestV:    current best value
    count:    
    '''
    n = 0
    value = []
    weight = []
    capacity = 0
    currentW = 0
    currentV = 0;
    select = []
    bestS = []
    bestV = 0
    count = 0

    def __init__(self,weight,value,capacity):
        self.weight = weight
        self.value = value
        self.capacity = capacity
        self.n = len(self.weight)
        try:
            self.n == len(value)
        except ValueError:
            print("Please check the number of weights and values.")
        self.bestS = self.select = [0]*self.n

def Backtrack(i,GP):
    if i >= GP.n:
        GP.count += 1
        if GP.currentW <= GP.capacity and GP.bestV < GP.currentV:
            GP.bestV = GP.currentV
            GP.bestS = GP.select[:]
        return
    GP.select[i] = 1
    GP.currentW += GP.weight[i]
    GP.currentV += GP.value[i]
    Backtrack(i+1,GP)
    
    GP.currentW -= GP.weight[i]
    GP.currentV -= GP.value[i]
    GP.select[i] = 0
    Backtrack(i+1,GP)

def TraverRun(weight=[6,5,4,1,2,3,9,8,7],value=[1,2,3,7,8,9,6,5,4],capacity=20):
    GP = Global(weight,value,capacity)
    Backtrack(0,GP)
    '''
    print("Number of accessing leaf nodes: ",GP.count)
    print("Selection; ",GP.bestS)
    print("Maximum value; ",GP.bestV)
    '''

if __name__ == '__main__':
    TraverRun()
