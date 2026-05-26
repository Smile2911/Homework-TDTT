# W9A1 - Duyệt cây theo thứ tự giữa (Inorder: Left → Root → Right)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# W9A2 - Duyệt cây theo thứ tự trước (Preorder: Root → Left → Right)
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# W9A3 - Duyệt cây theo thứ tự sau (Postorder: Left → Right → Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

# W9A4 - Tính chiều cao của cây (Height)
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

# W9A5 - Đếm số nút trong cây
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# W9A6 - Tính tổng giá trị các nút trong cây
def sum_nodes(root):
    if root is None:
        return 0
    return root.val + sum_nodes(root.left) + sum_nodes(root.right)

# W9A7 - Tìm giá trị lớn nhất trong cây
def find_max(root):
    if root is None:
        return float('-inf')
    return max(root.val, find_max(root.left), find_max(root.right))

# W9A8 - Kiểm tra hai cây có giống nhau hoàn toàn không
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))

# W9A9 - Kiểm tra cây có phải là cây tìm kiếm nhị phân (BST) không
def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if not (min_val < root.val < max_val):
        return False
    return (is_bst(root.left, min_val, root.val) and
            is_bst(root.right, root.val, max_val))
