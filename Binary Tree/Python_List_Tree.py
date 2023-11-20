# Common Operations on Tree
# 0. Creation of Tree
# 1. Insertion of Node
# 2. Searching for a value in Tree
# 3. Deletion of Node
# 4. Traversal all the nodes
# 5. Deletion of Tree

# Create Tree with Python List
# Rules for array:
# Root node will be at index 1
# Left Child will be at 2*Parent Index
# Right Child will be at 2*Parent Index + 1

############################
##### Creation of Tree #####
############################
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    #############################
    ##### Insertion of Node #####
    #############################
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full."
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted."
    
    #########################################
    ##### Searching for a value in Tree #####
    #########################################
    def searchNode(self, nodeValue):
        for i in range(1, len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"

    ##################################
    ##### Pre-Order Traversal ########
    ##################################
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    ##################################
    ##### In-Order Traversal #########
    ##################################
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)

    ##################################
    ##### Post-Order Traversal #######
    ##################################
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 + 1)
        print(self.customList[index])

    ##################################
    ##### Level-Order Traversal ######
    ##################################
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
    
    #######################
    ##### Delete Tree #####
    #######################
    def deleteTree(self):
        self.customList = None
        print("The Binary Tree has been successfully deleted.")

    #######################
    ##### Delete Node #####
    #######################
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete."
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted."


newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))
print(newBT.insertNode("Soup"))
print(newBT.insertNode("Cola"))
print(newBT.insertNode("Water"))

