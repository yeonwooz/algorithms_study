import sys

sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
matrix = []

def num_to_alphabet (a):
    y=''
    if a=='-1': y='A'
    elif a=='0': y='B'
    elif a=='1': y='C'
    
    return y

for i in range(N):
    matrix.append(list(map(num_to_alphabet, sys.stdin.readline().strip().split())))

def NineTree(i, j, l):
    if l==1:
        return matrix[i][j]
    else: 
        l=l//3
        nine_1 = NineTree(i, j, l)
        nine_2 = NineTree(i, j+l, l)
        nine_3 = NineTree(i, j+(2*l), l)
        nine_4 = NineTree(i+l, j, l)
        nine_5 = NineTree(i+l, j+l, l)
        nine_6 = NineTree(i+l, j+(2*l), l)
        nine_7 = NineTree(i+(2*l), j, l)
        nine_8 = NineTree(i+(2*l), j+l, l)
        nine_9 = NineTree(i+(2*l), j+(2*l), l)
        
        if nine_1 == nine_2 == nine_3 == nine_4 == nine_5 == nine_6 == nine_7 == nine_8 == nine_9 =='A': return 'A'
        elif nine_1 == nine_2 == nine_3 == nine_4 == nine_5 == nine_6 == nine_7 == nine_8 == nine_9 == 'B': return 'B'
        elif nine_1 == nine_2 == nine_3 == nine_4 == nine_5 == nine_6 == nine_7 == nine_8 == nine_9 == 'C': return 'C'
        else: 
            return nine_1+nine_2+nine_3+nine_4+nine_5+nine_6+nine_7+nine_8+nine_9

a = list(NineTree(0,0,N))
print(a.count('A'))
print(a.count('B'))
print(a.count('C'))