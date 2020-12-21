import sys
thisdict = {
  "RED": 1,
  "BLACK": 0
}

class Node():
    def __init__(self, value):
        self.value = value
        self.parent = self.left = self.right = None
        self.color = thisdict['RED']

class RedBlackTree():
    def __init__(self):
        self.val = Node(thisdict['BLACK'])
        self.val.color = thisdict['BLACK']
        self.val.left =self.val.right = None
        self.root = self.val #Assigns null node
    def getter_method(self,a,b):
        a=b
    l=[]
    def pre_order(self, node):
        if node != self.val:
            self.l.append((str(node.value) + " "))
            self.pre_order(node.left)
            self.pre_order(node.right)
    def compare_nodes(self,a,b):
        if a==b:
            return True
        else:
            return False

    def levelOrder(self):

        def dfs(node, res, level):
            if not node:
                return
            if len(res) == level:
                res.append([node.value])

            else:
                    res[level].append(node.value)

            dfs(node.left, res, level + 1)
            dfs(node.right, res, level + 1)

        res = []
        dfs(self.root, res, 0)
        return res

    def transplant(self, u, v):
        Parent=u.parent
        if Parent is None:
            self.root = v
        elif self.compare_nodes(u,Parent.right):
            Parent.right = v
        else:
            Parent.left = v
        v.parent = Parent

    def delete_node(self, node, key):
        z = self.val
        while self.compare_nodes(node,self.val)== False:
            if self.compare_nodes(node.value,key ):
                z = node

            if node.value <= key:
                node = node.right
            else:
                node = node.left



        if self.compare_nodes(z,self.val):
            return

        y = z
        y_original_color = y.color
        if z.left == self.val:
            x = z.right
            self.transplant(z, z.right)
        elif (z.right == self.val):
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.find_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if self.compare_nodes(y.parent,z)==False:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            else:
                x.parent = y


            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if self.compare_nodes(y_original_color,thisdict['BLACK']):
            while x != self.root and x.color == thisdict['BLACK']:
                if x == x.parent.left:
                    s = x.parent.right

                    if self.compare_nodes(s.left.color,thisdict['BLACK']) and self.compare_nodes(s.right.color,thisdict['BLACK']):
                        s.color = thisdict['RED']
                        x = x.parent
                    else:
                        if self.compare_nodes(s.right.color,thisdict['BLACK']):
                            s.left.color = thisdict['BLACK']
                            s.color = thisdict['RED']
                            self.right_rotate(s)
                            s = x.parent.right

                        s.color = x.parent.color
                        x.parent.color = thisdict['BLACK']
                        s.right.color = thisdict['BLACK']
                        self.left_rotate(x.parent)
                        x = self.root
                    if self.compare_nodes(s.color,thisdict['RED']):
                        s.color = thisdict['BLACK']
                        x.parent.color = thisdict['RED']
                        self.left_rotate(x.parent)
                        s = x.parent.right
                else:
                    s = x.parent.left
                    if self.compare_nodes(s.color,thisdict['RED']):
                        s.color = thisdict['BLACK']
                        x.parent.color = thisdict['RED']
                        self.right_rotate(x.parent)
                        s = x.parent.left

                    if self.compare_nodes(s.right.color,thisdict['BLACK']) and self.compare_nodes(s.right.color,thisdict['BLACK']):
                        s.color = thisdict['RED']
                        x = x.parent
                    else:
                        if self.compare_nodes(s.left.color,thisdict['BLACK']):
                            s.right.color = thisdict['BLACK']
                            s.color = thisdict['RED']
                            self.left_rotate(s)
                            s = x.parent.left

                        s.color = x.parent.color
                        x.parent.color = thisdict['BLACK']
                        s.left.color = thisdict['BLACK']
                        self.right_rotate(x.parent)
                        x = self.root
            x.color = thisdict['BLACK']


    def find_minimum(self, node):
        while node.left != self.val:
            node = node.left
        return node

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if self.compare_nodes(y.left,self.val)==False:
            y.left.parent = x

        y.parent = x.parent
        if self.compare_nodes(x.parent,None):
            self.root = y
        elif self.compare_nodes(x,x.parent.right):
            x.parent.right = y
        else:
            x.parent.left = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        p=x.parent
        if self.compare_nodes(y.right,self.val)==False:
            y.right.parent = x

        y.parent = p
        if self.compare_nodes(p,None):
            self.root = y
        elif self.compare_nodes(x,x.parent.left):
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y
    def init_insert(self,key):
        node = Node(key)
        node.parent ,node.value,node.color= None,key,thisdict['RED']
        node.left = node.right = self.val
        return node

    def insert(self, node_value):
        node=self.init_insert(node_value)
        y = None
        x = self.root

        while self.compare_nodes(x,self.val)==False:
            y = x
            if node.value > x.value:
                x = x.right
            else:
                x = x.left

        node.parent = y
        if self.compare_nodes(y,None):
            self.root = node
        elif node.value >y.value:
            y.right = node
        else:
            y.left = node

        if self.compare_nodes(y,None):
            node.color = thisdict['BLACK']
            return

        if self.compare_nodes(y.parent,None):
            return
        k=node
        w = k.parent

        while self.compare_nodes(w.color,thisdict['RED']):
            if self.compare_nodes(w,w.parent.right):
                u = w.parent.left
                if self.compare_nodes(u.color,thisdict['RED']):
                    w.parent.color = thisdict['RED']
                    k = w.parent
                    u.color = w.color = thisdict['BLACK']
                else:
                    if self.compare_nodes(k,w.left):
                        k = k.parent
                        self.right_rotate(k)
                    w.parent.color = thisdict['RED']
                    w.color = thisdict['BLACK']
                    self.left_rotate(w.parent)
            else:
                u = w.parent.right

                if self.compare_nodes(u.color,thisdict['RED']):
                    w.color = thisdict['BLACK']
                    w.parent.color = thisdict['RED']
                    u.color = thisdict['BLACK']
                    k = w.parent
                else:
                    if self.compare_nodes(k,w.right):
                        k = w
                        self.left_rotate(k)
                    w.color = thisdict['BLACK']
                    w.parent.color = thisdict['RED']
                    self.right_rotate(w.parent)
            if self.compare_nodes(k,self.root):
                break
        self.root.color = thisdict['BLACK']




    def deletion(self, value):
        self.delete_node(self.root, value)

    def get_height(self):
        root=self.root
        def helper(root):
            if not root:
                return -1
            left_height = helper(root.left)
            right_height = helper(root.left)
            return max(left_height, right_height) + 1
        return(helper(root))


if __name__ == "__main__":
    bst = RedBlackTree()
    arr = []
    with open(sys.argv[1]) as f:
        content = f.read().splitlines()
    for x in content:
        arr.append([int(x) for x in x.split()])
    #print(arr)
    print("Node  Height")
    print("(0,  0)")		
    j = 1
    #print(str(bst.get_height()))
    for i in arr[0]:
        bst.insert(i)
        print(j,str(bst.get_height()))
        j += 1
    #bst.deletion(arr[0][10])
    #bst.print_tree()
    #print(bst.levelOrder())
