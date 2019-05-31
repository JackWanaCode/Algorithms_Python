from random import shuffle

class Node:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.tree = None
        self.size = 0

    
    def put(self, key):
        new_node = Node(key)
        if self.tree:
            self._put(self.tree, new_node)
        else:
            self.tree = new_node
        self.size += 1

    def _put(self, current_node, new_node):
        if new_node.key < current_node.key:
            if current_node.left:
                self._put(current_node.left, new_node)
            else:
                current_node.left = new_node
                new_node.parent = current_node
        else:
            if current_node.right:
                self._put(current_node.right, new_node)
            else:
                current_node.right = new_node
                new_node.parent = current_node.right

    def remove(self, val):
        if self.root:
            self._remove(self.root, val)
    
    def _remove(self, current_node, val):
        if val == current_node.info:
            

    def depth(self, node):
        count = 0
        if node.parent:
            count += 1
            self.depth(node.parent)
        return count

    def height(self):
        if self.tree == None:
            return 0
        h =  height(self.left) if (height(self.left > height(self.right) + 1)) else height(self.right) + 1
        return h

    def pre_order_travel(self, root):
        if root:
            print(root.key, end=' ')
            self.pre_order_travel(root.left)
            self.pre_order_travel(root.right)

    def in_order_travel(self, root):
        if root:
            self.in_order_travel(root.left)
            print(root.key, end=' ')
            self.in_order_travel(root.right)

    def post_order_travel(self, root):
        if root:
            self.post_order_travel(root.left)
            self.post_order_travel(root.right)
            print(root.key, end=' ')

    def level_order_travel(self, root):
        if root:
            queue = [root]
            while(queue):
                node = queue.pop(0)
                print(node.key, end=' ')
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(arr)
print(arr)
root = BinarySearchTree()
for num in arr:
    root.put(num)

root.pre_order_travel(root.tree)
print('')
root.in_order_travel(root.tree)
print(' ')
root.post_order_travel(root.tree)
print(' ')
root.level_order_travel(root.tree)
print(' ')

