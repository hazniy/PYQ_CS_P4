ArrayNodes = [[-1 for i in range(3)]for j in range(20)]
print(ArrayNodes)

freenodes = 6
rootpointer = 0
ArrayNodes[0][0] = 1
ArrayNodes[0][1] = 20
ArrayNodes[0][2] = 5
ArrayNodes[1][0] = 2
ArrayNodes[1][1] = 15
ArrayNodes[2][1] = 3
ArrayNodes[2][2] = 3
ArrayNodes[3][1] = 9
ArrayNodes[3][2] = 4
ArrayNodes[4][1] = 10
ArrayNodes[5][1] = 58
print(ArrayNodes)

def SearchValue(root,valfind):
    if root == -1:
        return -1
    else:
        if ArrayNodes[root][1] == valfind:
            return root
        else:
            if ArrayNodes[root][1] == -1:
                return -1
    if ArrayNodes[root][1] > valfind:
        return SearchValue(ArrayNodes[root][0], valfind)
    if ArrayNodes[root][1] < valfind:
        return SearchValue(ArrayNodes[root][2], valfind)

def PostOrder():

#main
data = SearchValue(0,15)
if data == -1:
    print('not found')
else:
    print(data)
PostOrder()
