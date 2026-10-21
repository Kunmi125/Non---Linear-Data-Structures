class Binary_Tree_Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def inorder_traversal(self):
        if self.left:
            print(self.left.inorder_traversal())
        print(self.data)
        if self.right:
            print(self.right.inorder_traversal())

root = Binary_Tree_Node(1)
root.left = Binary_Tree_Node(2)
root.right = Binary_Tree_Node(3)

root.left.left = Binary_Tree_Node(4)
root.left.right = Binary_Tree_Node(5)

root.right.right = Binary_Tree_Node(6)

root.inorder_traversal()




    