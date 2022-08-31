from typing import Iterable, List


class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.value = val
        
        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        if node is not None:
            assert isinstance(node, TreeNode)
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if node is not None:
            assert isinstance(node, TreeNode)
        self._right = node

    @property
    def is_leaf(self):
        return self._left is None and self._right is None

    @property
    def is_fully_branch(self):
        return self._left is not None and self._right is not None

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self):
        self.root = None

    @property
    def is_empty(self) -> bool:
        return self.root is None

    def batch_insert(self, values: Iterable):
        for val in values:
            self.insert(val)

    def insert(self, value):
        if self.is_empty:
            self.root = TreeNode(value)
        else:
            self.root = self._insert_recur(value, self.root)

    def remove(self, value):
        if self.is_empty:
            raise ValueError("Tree is empty")
        else:
            self.root = self._remove_recur(value, self.root)

    def find(self, value):
        if self.is_empty:
            return None
        else:
            iter = self.root

            while iter is not None:
                if iter.value == value:
                    break
                elif value < iter.value:
                    iter = iter.left
                else:
                    iter = iter.right

            return iter

    def tolist(self, mode="preorder"):
        """
        Convert a binary tree to a list

        Args:
            mode: "preorder", "inorder" or "postorder"

        Return:
            list: List with order of traversal
        """

        if mode == "preorder":
            return self._preorder_traversal(self.root)
        elif mode == "inorder":
            return self._inorder_traversal(self.root)
        elif mode == "postorder":
            return self._postorder_traversal(self.root)
        else:
            raise ValueError("Invalid mode")

    def _preorder_traversal(self, node: TreeNode) -> List:
        if node is None:
            return []
        else:
            return [node.value]\
                    + self._preorder_traversal(node.left)\
                    + self._preorder_traversal(node.right)

    def _inorder_traversal(self, node: TreeNode) -> List:
        if node is None:
            return []
        else:
            return self._inorder_traversal(node.left)\
                    + [node.value]\
                    + self._inorder_traversal(node.right)

    def _postorder_traversal(self, node: TreeNode) -> List:
        if node is None:
            return []
        else:
            return self._postorder_traversal(node.left)\
                    + self._postorder_traversal(node.right)\
                    + [node.value]

    def _remove_recur(self, value, cur_node: TreeNode):
        if cur_node is None:
            raise ValueError("The value is not in the tree")
        elif value < cur_node.value:
            cur_node.left = self._remove_recur(value, cur_node.left)
        elif value > cur_node.value:
            cur_node.right = self._remove_recur(value, cur_node.right)
        else:
            if cur_node.is_leaf:
                return None
            elif cur_node.is_fully_branch:
                # find the most depth-left of the right node
                parent_rep_node = None
                rep_node = cur_node.right
                while rep_node.left is not None:
                    parent_rep_node = rep_node
                    rep_node = rep_node.left
                
                # copy data of rep_node to cur_node
                # and remove rep_node instead
                cur_node.value = rep_node.value
                parent_rep_node.left = self._remove_recur(rep_node.value, parent_rep_node.left)
            elif cur_node.left is not None:
                return cur_node.left
            else:
                return cur_node.right

        return cur_node
    
    def _insert_recur(self, value, cur_node: TreeNode) -> TreeNode:
        if cur_node is None:
            return TreeNode(value)
        elif value < cur_node.value:
            cur_node._left = self._insert_recur(value, cur_node._left)
        elif value > cur_node.value:
            cur_node._right = self._insert_recur(value, cur_node._right)

        return cur_node