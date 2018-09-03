class Node :
    def __init__(self,val):
        self.data = val 
        self.next = None
def Insert(arr):
    ''' create circular link list '''
    head = Node(arr[0])
    temp = head
    for val in range(1,len(arr)):
        temp.next = Node(arr[val])
        temp = temp.next 
    temp.next = head
    return head 
def printList(head,numOfNode):
    temp = head 
    count = 0
    ansList = []
    while (count != numOfNode):
        ansList.append(temp.data)
        temp = temp.next 
        count+=1
    print(ansList)

N = int(input('input N: '))
M = int(input('input M: '))
dataArr = [val for val in range(1,(2*N)+1)]
head = Insert(dataArr)
point = head 
N_puls_one = N+1
N_double = 2*N
N_puls_one_status = False 
N_double_status = False   
numOfNode = len(dataArr)   
while(N_double_status == False or N_puls_one_status==False) :
    for val in range(M-1):
        pre_point = point
        point=point.next 
    if point.data == N_puls_one :
        N_puls_one_status = True 
    if point.data == N_double:
        N_double_status = True 

    pre_point.next = point.next
    point=point.next
    numOfNode = numOfNode-1

printList(head,numOfNode)


