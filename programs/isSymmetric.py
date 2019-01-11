class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root == None:
            return True
        return self.isSymmeticNode(root.left,root.right)

    def isSymmeticNode(self, left,right):
        if left == None and right == None :
            return True
        if left ==  None or right == None or left.val != right.val :
            return False
        return self.isSymmeticNode(left.left,right.right) and self.isSymmeticNode(left.right, right.left)