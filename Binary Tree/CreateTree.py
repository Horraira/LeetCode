# basic tree structure
class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def add_child(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode("Drinks", [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
fanta = TreeNode('Fanta', [])
cola = TreeNode('Cola', [])
tree.add_child(cold)
tree.add_child(hot)
cold.add_child(fanta)
cold.add_child(cola)
print(tree)