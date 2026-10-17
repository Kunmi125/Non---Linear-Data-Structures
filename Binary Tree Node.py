class Binary_Tree_Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def traverse_inorder(self):
        
        elements = []
        if self.left:
            elements += self.left.traverse_inorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.traverse_inorder()
        return elements

root = Binary_Tree_Node(3)
root.left = Binary_Tree_Node(5)
root.left.left = Binary_Tree_Node(6)
root.left.right = Binary_Tree_Node(7)

root.right = Binary_Tree_Node(4)
root.right.left = Binary_Tree_Node(2)





print("In-order Traversal:", root.traverse_inorder())