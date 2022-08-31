from gnaoh import *

if __name__ == '__main__':
    tree = BinaryTree()
    tree.batch_insert([3, 1, 2, 5, 4])
    tree.remove(5)

    print(tree.tolist(mode="preorder"))