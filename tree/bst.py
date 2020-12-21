from random import randint
import sys
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
def deletion(root,key):
    if root is None:
        return root
    if key > root.val:
        root.right = deletion(root.right, key)
    elif (key < root.val):
        root.left = deletion(root.left, key)
    else:
        if root.right == None:
            temp = root.left
            root = None
            return temp

        elif root.left == None:
            temp = root.right
            root = None
            return temp
        current = root.right
        while (current.left is not None):
            current = current.left
        temp = current
        root.val= temp.val
        root.right = deletion(root.right, temp.val)

    return root



def height(root):
    if not root:
        return -1
    left_height=height(root.left)
    right_height=height(root.right)
    return max(left_height,right_height)+1

if __name__ == "__main__":
    '''
    r=Node(0)
    for x in range(10,100,5):
        for i in range((x)):
            value=randint(1,1000)
            val = insert(r, value)
        h = height(val)
        print(x,h)

    '''
    arr=[]
    with open(sys.argv[1]) as f:
        content = f.read().splitlines()
    for x in content:
        arr.append([int(x) for x in x.split()])
    print("Nodes Height")
    r = Node(arr[0][0])
    h = height(r)
    print("(0, "+str(h)+")")
    j=1
    for i in  arr[0][1:]:
        val = insert(r, i)
        h = height(val)
        print(j,h)
        j+=1
    #print(h)
    #deletion(r,arr[0][3])

