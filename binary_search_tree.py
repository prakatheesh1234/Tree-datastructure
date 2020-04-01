
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



def insert(root,data):
    if data !=None:
        if data <root.data:
            if root.left is None:
                root.left=node(data)
            else:
                insert(root.left,data)
        if data >root.data:
            if root.right is None:
                root.right=node(data)
            else:
                insert(root.right,data)
    else:
         root=data
         

  
 
def inorder(root):
   if root:
       inorder(root.left)
       print(root.data)
       inorder(root.right)
       



def pre_order(root):
   if root:
       
       print(root.data)
       inorder(root.left)
       inorder(root.right)
        
       
       
       



def post_order(root):
   if root:
       
      
       inorder(root.left)
       inorder(root.right)
       print(root.data)
       
       
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
root=node(34)

root.left=node(23)
root.right=node(50)
insert(root,21)
insert(root,89)
insert(root,1)
insert(root,2)
insert(root,56)
insert(root,76)
insert(root,30)
print("Inorder") 
print("\n")
inorder(root)
print("Pre order")
print("\n")
pre_order(root)
print("Post order")
print("\n")
post_order(root)