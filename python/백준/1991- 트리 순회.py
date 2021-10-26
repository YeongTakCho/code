class binary_tree:

    class Node:
        def __init__ (self, data):
            self.data :str = data
            self.left : self.Node = None
            self.right : self.Node = None
    def putdata(self):
        self.root = self.Node('A')
        data_dict :dict[str, self.Node]= {
            'A' : self.root
        }

        N = int(input())

        for _ in range(N):
            parent, left, right = input().split()
            if left != '.':
                data_dict[parent].left = self.Node(left)
                data_dict[left] = data_dict[parent].left

            if right != '.':
                data_dict[parent].right = self.Node(right)
                data_dict[right] = data_dict[parent].right

    def preorder(self):
        def _preorder(parentNode : self.Node):
            print(parentNode.data, end='')
            if parentNode.left:
                _preorder(parentNode.left)
            if parentNode.right:
                _preorder(parentNode.right)
        _preorder(self.root)

    def inorder(self):
        def _inorder(parentNode: self.Node):
            if parentNode.left:
                _inorder(parentNode.left)
            print(parentNode.data, end= '')
            if parentNode.right:
                _inorder(parentNode.right)
        _inorder(self.root)

    def postorder(self):
        def _postorder(parentNode: self.Node):
            if parentNode.left:
                _postorder(parentNode.left)
            if parentNode.right:
                _postorder(parentNode.right)
            print(parentNode.data, end= '')
        _postorder(self.root)
        

 
tree = binary_tree()
tree.putdata()

tree.preorder(); print()
tree.inorder(); print()
tree.postorder()