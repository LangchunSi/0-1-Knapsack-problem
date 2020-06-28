# Dynamic programming method
'''
# mainRun(weight,value,capacity,type)

    n:        number of items
    value:    value of each item
    weight:   weight of each item
    capacity: capacity of bag
    m:        memery matrix
    type: 'right2left' or 'left2right'
'''

# right to left
def Knapsack(value,weight,capacity,n,m):
    jMax = min(weight[n-1]-1,capacity)
    for j in range(0,jMax+1):
        m[n-1][j] = 0
    for j in range(weight[n-1],capacity+1):
        m[n-1][j] = value[n-1]
    for i in range(n-2,-1,-1):
        jMax = min(weight[i]-1,capacity+1)
        for j in range(0,jMax+1):
            m[i][j] = m[i+1][j]
        for j in range(weight[i],capacity+1):
            m[i][j] = max(m[i+1][j],m[i+1][j-weight[i]]+value[i])
    return m

def Trackback(m,weight,capacity,n,select):
    for i in range(0,n-1):
        if m[i][capacity] == m[i+1][capacity]:
            select[i] = 0
        else:
            select[i] = 1
            capacity = capacity - weight[i]
    if m[n-1][capacity] != 0:
        select[n-1] = 1
    return select

# left to right
def KnapsackL(value,weight,capacity,n,m):
    jMax = min(weight[0]-1,capacity)
    for j in range(0,jMax+1):
        m[0][j] = 0
    for j in range(weight[0],capacity+1):
        m[0][j] = value[0]
    for i in range(1,n,1):
        jMax = min(weight[i]-1,capacity+1)
        for j in range(0,jMax+1):
            m[i][j] = m[i-1][j]
        for j in range(weight[i],capacity+1):
            m[i][j] = max(m[i-1][j],m[i-1][j-weight[i]]+value[i])
    return m

def TrackbackL(m,weight,capacity,n,select):
    for i in range(n-1,0,-1):
        if m[i][capacity] == m[i-1][capacity]:
            select[i] = 0
        else:
            select[i] = 1
            capacity = capacity - weight[i]
    if m[0][capacity] != 0:
        select[0] = 1
    return select

# switch between left2right and right2left
def switchFunc(value,weight,capacity,n,m,Select,type):
    if type == 'right2left':
        # print('Type: right to left.')
        m = Knapsack(value,weight,capacity,n,m)
        select = Trackback(m,weight,capacity,n,Select)
    else:
        # print('Type: left to right.')
        m = KnapsackL(value,weight,capacity,n,m)
        select = TrackbackL(m,weight,capacity,n,Select)
    return m, select

def mainRun(weight = [6,5,4,1,2,3,9,8,7],value = [1,2,3,7,8,9,6,5,4],capacity = 20,type = 'left2right'):
    '''
    weight = [6,5,4,1,2,3,9,8,7]
    value = [1,2,3,7,8,9,6,5,4]
    capacity = 20
    '''
    '''
    weight = [3, 5, 1, 4, 2, 6]
    value = [2, 3, 4, 2, 5, 1]
    capacity = 11
    '''

    n = len(weight)
    try:
        n == len(value)
    except ValueError:
        print("Please check the number of weights and values.")
    m = [[-1]*(capacity+1) for _ in range(n)]
    select = [0 for _ in range(n)]
    
    (m,select) = switchFunc(value,weight,capacity,n,m,select,type)
    
    maxValue = 0;
    for i in range(0,n):
        if select[i] == 1:
            maxValue = maxValue + value[i]
    '''
    print("Dymamic programming method is done.")
    print("m matrix: ", m)
    print("Select: ",select)
    print("Maximum value: ",maxValue,"\n")
    '''
    

if __name__ == '__main__':
    mainRun(type = 'right2left')
    mainRun(type = 'left2rightt')

