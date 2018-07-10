def merge(a,b):
	if a==None:
		return b
	
	if b==None:
		return a
	
	if(a.data< b.data):
		result=a
		result.down=merge(a.down,b)
	
	else:
		result=b
		result.down=merge(a,b.down)
		
	return result

def flattten(root):
	if root==None or root.right==None:
		return root
	merge(root, flatten(root.right))
	