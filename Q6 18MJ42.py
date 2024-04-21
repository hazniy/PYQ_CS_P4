# Write a recursive function, in program code, to traverse the binary tree and output the value of DataValue for each leaf node.
#q6 binary tree
def FindLeaves(CurrentNode):
    global BinaryTree
    if(BinaryTree[CurrentNode].LeftPointer != -1):
        FindLeaves(BinaryTree[CurrentNode].LeftPointer)
    if(BinaryTree[CurrentNode].RightPointer != -1):
        FindLeaves(BinaryTree[CurrentNode].RightPointer)
    if((BinaryTree[CurrentNode].RightPointer == -1) and (BinaryTree[CurrentNode].LeftPointer == -1)):
        print(BinaryTree[CurrentNode].DataValue)
    return 
