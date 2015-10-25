import components.TreeNode as Node
import queueaslinkedlist.QueueAsLinkedList as Queue


class BinaryTree:
    root = None

    def add(self, val):
        if self.root is None:
            new = Node.TreeNode(val)
            self.root = new
        else:
            current = self.root
            while current.value is not None:  # while we're inside a node with a value already, find a lower node
                if val > current.value:  # if new value is greater than current value, step right
                    if current.right is None:
                        current.right = Node.TreeNode(val)
                        return
                    else:
                        current = current.right
                elif val < current.value:  # if new value is less than current value, step left
                    if current.left is None:
                        current.left = Node.TreeNode(val)
                        return
                    else:
                        current = current.left

    def search(self, val):
        """Return the value you're searching for in O(log(n))"""
        if self.root is None:
            return None
        else:
            return self.recursive_search(self.root, val)

    @staticmethod
    def recursive_search(root, val):
        """Search the current tree for the key
        Will return the key if it's found, None otherwise. Returned node may or may not contain a 'value' component"""
        current = root
        while current.left is not None or current.right is not None:  # until we hit a leaf node, traverse the tree
            if current.data == val:
                return current.data
            elif current.data > val:
                current = current.left
            else:
                current = current.right
        return None

    def print_breadth_first(self):
        if self.root is None:
            return
        else:
            queue = Queue.QueueAsLinkedList()
            queue.enqueue(self.root)
            while queue.peek() is not None:
                current_node = queue.dequeue()
                current_node.data.print()
                if current_node.data.left is not None:
                    queue.enqueue(current_node.data.left)
                if current_node.data.right is not None:
                    queue.enqueue(current_node.data.right)

    def print_depth_first_post_order(self):
        if self.root is None:
            return
        else:
            self.depth_first_post_order_print(self.root)

    def print_depth_first_pre_order(self):
        if self.root is None:
            return
        else:
            self.depth_first_pre_order_print(self.root)

    def print_depth_first_in_order(self):
        if self.root is None:
            return
        else:
            self.depth_first_in_order_print(self.root)

    def depth_first_pre_order_print(self, tree):
        tree.print()
        if tree.left is not None:
            self.depth_first_pre_order_print(tree.left)
        if tree.right is not None:
            self.depth_first_pre_order_print(tree.right)

    def depth_first_in_order_print(self, tree):
        if tree.left is not None:
            self.depth_first_in_order_print(tree.left)
        tree.print()
        if tree.right is not None:
            self.depth_first_in_order_print(tree.right)

    def depth_first_post_order_print(self, tree):
        if tree.left is not None:
            self.depth_first_post_order_print(tree.left)
        if tree.right is not None:
            self.depth_first_post_order_print(tree.right)
        tree.print()

    def delete_value(self, node, value):
        if node is None:
            return
        elif value < node.value:
            node.left = self.delete_value(node.left, value)
        elif value > node.value:
            node.right = self.delete_value(node.right, value)
        else:
            # case 1 : no child
            if node.left is None and node.right is None:
                del node
            elif node.left is None:
                print ("left tree empty")
            elif node.right is None:
                print ("right tree empty")
            else:
                print ("neither tree empty")
