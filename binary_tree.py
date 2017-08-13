class Node():
	def __init__(self,value):
		self.left=None
		self.right=None
		self.value=value
node=Node(9)
node1=Node(3)
node2=Node(4)
node4=Node(5)
node3=Node(48)
node5=Node(5)
node6=Node(2)
class binary_tree():
	def __init__(self,node):
		self.root=node
	
	def __insert_with_root(self,root,node):
		if(root.value > node.value):
			if(root.left != None):
				self.__insert_with_root(root.left,node)
			else:
				root.left=node
		else:		
			if(root.right != None):
				self.__insert_with_root(root.right,node)
			else:
				root.right=node
						
	def insert(self,node):
		self.__insert_with_root(self.root, node)

	def check(self,root):
		leftvalid=True
		rightvalid=True
		if root.left:
			if root.left<root.value:
				leftvalid=True
			leftvalid=False
		else:
			leftvalid=True
		if root.right:
			if root.right>root.value:
				rightvalid=True
			rightvalid=False
		else:
			rightvalid=True

		if(leftvalid & rightvalid):
			return check(root.left)&check(root.right)

		return leftvalid&rightvalid





binary=binary_tree(node)
binary.insert(node1)
binary.insert(node2)
binary.insert(node3)
binary.insert(node4)
binary.insert(node5)
binary.insert(node6)
print(binary.check(node))