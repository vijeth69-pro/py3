class Node:
    def __init__(self):
        self.key = int(input("Enter node value: "))
        self.left = None
        self.right = None

    def min_node(self):
        if self.left is None:
            return self
        return self.left.min_node()

    def max_node(self):
        if self.right is None:
            return self
        return self.right.max_node()

    def preorder(self):
        print(self.key, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key, end=' ')

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right:
            self.right.inorder()

    def insert_tree(root, n):
        if root is None:
            return n
        elif n.key <= root.key:
            root.left = Node.insert_tree(root.left, n)
        else:
            root.right = Node.insert_tree(root.right, n)
        return root


    def delete_tree(root, v):
        if root is None:
            return root
        if v < root.key:
            root.left = Node.delete_tree(root.left, v)
        elif v > root.key:
            root.right = Node.delete_tree(root.right, v)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = root.right.min_node()
            root.key = temp.key
            root.right = Node.delete_tree(root.right, temp.key)
        return root

    def search(root, v, l):
        if root is None:
            return None
        if root.key == v:
            return l
        elif v < root.key:
            return Node.search(root.left, v, l + 1)
        else:
            return Node.search(root.right, v, l + 1)

    def dfs(root):
        if root is None:
            return
        stack = [root]
        while stack:
            e = stack.pop()
            print(e.key, end=' ')
            if e.right:
                stack.append(e.right)
            if e.left:
                stack.append(e.left)

    def bfs(root):
        if root is None:
            return
        queue = [root]
        while queue:
            e = queue.pop(0)
            print(e.key, end=' ')
            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)

if __name__ == '__main__':
    t = None
    while True:
        print("\n1: Insert Tree\n2: Delete Tree\n3: Search\n4: Min Node\n5: Max Node\n6: Preorder\n7: Postorder\n8: Inorder\n9: DFS\n10: BFS\n11: Exit")
        opt = int(input("Enter your choice: "))
        if opt == 1:
            n = Node()
            t = Node.insert_tree(t, n)
        elif opt == 2:
            v = int(input("Enter value to delete: "))
            t = Node.delete_tree(t, v)
        elif opt == 3:
            v = int(input("Enter value to search: "))
            l = Node.search(t, v, 0)
            if l is None:
                print(v, "not found")
            else:
                print(v, "found at level", l)
        elif opt == 4:
            if t:
                print("Min node:", t.min_node().key)
            else:
                print("Tree is empty.")
        elif opt == 5:
            if t:
                print("Max node:", t.max_node().key)
            else:
                print("Tree is empty.")
        elif opt == 6:
            if t:
                print("Preorder traversal:")
                t.preorder()
                print()
            else:
                print("Tree is empty.")
        elif opt == 7:
            if t:
                print("Postorder traversal:")
                t.postorder()
                print()
            else:
                print("Tree is empty.")
        elif opt == 8:
            if t:
                print("Inorder traversal:")
                t.inorder()
                print()
            else:
                print("Tree is empty.")
        elif opt == 9:
            if t:
                print("DFS traversal:")
                Node.dfs(t)
                print()
            else:
                print("Tree is empty.")
        elif opt == 10:
            if t:
                print("BFS traversal:")
                Node.bfs(t)
                print()
            else:
                print("Tree is empty.")
        elif opt == 11:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
