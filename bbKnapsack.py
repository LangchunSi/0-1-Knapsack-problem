# Branch and bound method
import queue

class Node:
    '''
    upbound: upbound value of node
    value:   value of current node
    weight:  weight of current node
    level:   level number of the current node on the subset tree
    '''
    upbound = 0
    value = 0
    weight = 0
    level = 0
    def __init__(self,cupbound,cvalue,cweight,clevel):
        self.upbound = cupbound
        self.value = cvalue
        self.weight = cweight
        self.level = clevel

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
    count:    number of accessing leaf node
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
    heap = queue.LifoQueue()
    
    
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

    def maxBound(self,i):
        cleft = self.capacity - self.currentW
        bound = self.currentV
        while i < self.n and self.weight[i] <= cleft:
            cleft -= self.weight[i]
            bound += self.value[i]
            i += 1
        if i < self.n:
            bound += self.perV[i]*cleft
        return bound

    def addLiveNode(self,cupbound,cvalue,cweight,clevel):
        node = Node(cupbound,cvalue,cweight,clevel)
        if clevel < self.n:
            self.heap.put(node)

    def knapsack(self,i):
        upbound = self.maxBound(i);
        while True:
            wt = self.currentW + self.weight[i]
            if wt <= self.capacity:
                if self.currentV + self.value[i] > self.bestP:
                    self.bestP = self.currentV + self.value[i]
                self.addLiveNode(upbound,self.currentV+self.value[i],self.currentW+self.weight[i],i+1)
            upbound = self.maxBound(i+1)
            if upbound >= self.bestP:
                self.addLiveNode(upbound,self.currentV,self.currentW,i+1)
            if self.heap.empty():
                return
            node = self.heap.get()
            self.currentW = node.weight
            self.currentV = node.value
            upbound = node.upbound
            i = node.level
            if i == self.n-1:
                self.count += 1

def BranchBoundRun(weight = [2,5,4,1,6,3,9,8,7],value = [8,2,3,7,1,9,6,5,4],capacity = 20):
    GP = Global(capacity,value,weight)
    GP.knapsack(0)
    n = GP.heap.qsize()
    # trueSelect = [0]*GP.n
    '''
    print("Number of accessing leaf nodes: ",GP.count)
    print("Maximum value = ",GP.bestP)
    '''

if __name__ == '__main__':
    BranchBoundRun()
