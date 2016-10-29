#!/usr/bin/python

"""An implementation of AVL tree in Python 3.5.1
   Code by: Humayun Kabir, humayun.k1@gmail.com"""

class AVLTree:
    """An AVL tree implementation"""
    class Node:
        """Node class - attributes are: value, left child, right child and height"""
        __slots__ = '_left', '_value', '_right', '_height'
        def __init__(self, l, v, r):
            """Construct of Node"""
            self._left = l
            self._value = v
            self._right = r
            self._height = 1

    def __init__(self):
        """Constructor of AVL Tree -- creates an empty tree"""
        self._root = None

    def insert(self, value):
        """Inserts a value in the tree"""
        self._root = self._rec_insert(self._root, value)

    def max(self):
        """Finds the maximum value in the tree"""
        return self._recMax(self._root)

    def _recMax(self, here):
        """Finds the maximum value in a tree rooted at 'here' """
        if here._right is None:
            return here._value
        else:
            return self._recMax(here._right)

    def min(self):
        """Finds the minimum value in the tree"""
        return self._recMin(self._root)

    def _recMin(self, here):
        """Finds the minimum value in a tree rooted at 'here'"""
        if here._left is None:
            return here._value
        else:
            return self._recMin(here._left)

    def search(self, value):
        """Searches for 'value' in the tree"""
        return self._recSearch(self._root, value)

    def _recSearch(self, here, value):
        """Recursively searches for 'value' in a tree rooted at 'here'"""
        if here is None:
            return None
        elif value < here._value:
            return self._recSearch(here._left, value)
        elif value > here._value:
            return self._recSearch(here._right, value)
        else:
            return here
        
    #Utility functions
    def _max(self, a, b):
        """Computes the maximum of a and b"""
        if a > b:
            return a
        else:
            return b

    def _getHeight(self, here):
        """Computes the height of a tree rooted at 'here'"""
        if here is None:
            return 0
        else:
            return here._height
        
    def _getBalance(self, here):
        """Get the balance factor of a a tree rooted at 'here'"""
        if here is None:
            return 0
        else:
            return self._getHeight(here._left) - self._getHeight(here._right) 
                    
    def _rec_insert(self, here, value):
        """Inserts 'value' in a tree rooted at 'here'"""
        #First inserts the value
        if here is None:
            return self.Node(None, value, None)
        elif value < here._value:
            here._left = self._rec_insert(here._left, value)
        else:
            here._right = self._rec_insert(here._right, value)

        #Update the height of this node
        here._height = self._max( self._getHeight(here._left), self._getHeight(here._right)) + 1

        #Get the balance factor of this node
        factor = self._getBalance(here)

        #Check if this node has become unbalanced
        #left-left-case -- needs a right-rotation
        if factor > 1 and value < here._left._value:
            return self._rightRotate(here)
        
        #right-right-case -- needs a left-rotation
        elif factor < -1 and value > here._right._value:
            return self._leftRotate(here)
        
        #left-right-case -  needs two rotations
        #a left rotation followed by a right rotation
        elif factor > 1 and value > here._left._value:
            here._left = self._leftRotate(here._left)
            return self._rightRotate( here )
        
        #right-left-case - needs two rotations
        #a right rotation followed by a left rotation
        elif factor < -1 and value < here._right._value:
            here._right = self._rightRotate(here._right)
            return self._leftRotate( here )
        
        #Return the unchanged node
        return here

    def __iter__(self):
        """Defines iterator for the tree -- inorder traversal"""
        if self._root is not None:
            yield from self._rec_iter(self._root)

    def _rec_iter(self, here):
        if here is not None:
            yield from self._rec_iter(here._left)
            yield here._value
            yield from self._rec_iter(here._right)

    def preOrder(self):
        """Finds the pre-order traversal of the tree"""
        self._preOrder(self._root)

    def _preOrder(self, here):
        """Finds the pre-order traversal of a tree rooted at 'here'"""
        if here is not None:
            print(here._value, end = " ")
            self._preOrder(here._left)
            self._preOrder(here._right)

    def __str__(self):
        return " ".join( str(i) for i in iter(self)) 

    def _rightRotate(self, y):
        """Right rotate a tree rooted at 'y'"""
        x = y._left
        T2 = x._right

        #perform rotation
        x._right = y
        y._left = T2

        #Update heights
        y._height = self._max( self._getHeight(y._left), self._getHeight(y._right)) + 1
        x._height = self._max( self._getHeight(x._left), self._getHeight(x._right)) + 1

        #return new root
        return x

    def _leftRotate(self, y):
        """Left rotate a tree rooted at y"""
        x = y._right
        T2 = x._left

        #perform rotation
        x._left = y
        y._right = T2

        #Update heights
        y._height = self._max( self._getHeight(y._left), self._getHeight(y._right) ) + 1
        x._height = self._max( self._getHeight(x._left), self._getHeight(x._right) ) + 1
        
        #return new root
        return x

    def minNode(self):
        """Finds the node with the minimum value in the tree"""
        return self._recMinNode(self._root)

    def _recMinNode(self, here):
        """Finds the minimum node rooted at tree 'here'"""
        if here._left is None:
            return here
        else:
            return self._recMinNode(here._left)

    def delete(self, value):
        """Deletes a node containing 'value'"""
        self._root = self._recDelete(self._root, value)

    def _recDelete(self, here, value):
        """Deletes a node containing 'value' from tree rooted at 'here'""" 
        #Delete the node 
        if here is None:
            return None
        #value is smaller than here's value
        elif value < here._value:
            here._left = self._recDelete(here._left, value)
        #value is greater than here's value    
        elif value > here._value:
            here._right = self._recDelete(here._right, value)
        else:
            #Node has right child
            if here._left is None:
                temp = here._right
                here = temp

            #Node has left child    
            elif here._right is None:
                temp = here._left
                here = temp
                
            #both children are None    
            elif (here._right is None) and (here._left is None):
                here = None
                
            else:
                #Node with two children: Get the inorder successor
                #smallest in the right subtree
                temp = self._recMinNode(here._right)
                here._value = temp._value

                #Delete the inorder successor
                here._right = self._recDelete(here._right, temp._value)
                
        #if the tree had only one node then return
        if here is None:
            return here

        #Update height of the node
        here._height = self._max( self._getHeight(here._left), self._getHeight(here._right)) + 1

        #Get the balance factor of this node
        factor = self._getBalance( here )

        #If this node becomes unbalanced
        #LEFT-LEFT-CASE - right rotate
        if factor > 1 and self._getBalance(here._left) >= 0:
            return self._rightRotate(here)

        #LEFT-RIGHT-CASE -- two rotations are needed
        #left rotate, followed by right rotate
        if factor > 1 and self._getBalance(here._left) < 0:
            here._left = self._leftRotate(here._left)
            return self._rightRotate( here )

        #RIGHT-RIGHT-CASE -- left rotate
        if factor < -1 and self._getBalance(here._right) <= 0:
            return self._leftRotate(here)

        #RIGHT-LEFT-CASE -- two rotations are needed
        #right rotate, followed by left rotate 
        if factor < -1 and self._getBalance(here._right) > 0:
            here._right = self._rightRotate(here._right)
            return self._leftRotate( here )

        return here
        
#Test the code
if __name__ == '__main__':
    aTree = AVLTree()

    aTree.insert(9)
    aTree.insert(5)
    aTree.insert(10)
    aTree.insert(0)
    aTree.insert(6)
    aTree.insert(11)
    aTree.insert(-1)
    aTree.insert(1)
    aTree.insert(2)

    print("Preorder traversal of the AVL tree")
    aTree.preOrder()

    print("\nMin is: ", aTree.min() )
    print("Max is: ", aTree.max() )

    val = 10
    aTree.delete( val )

    print("\n Pre-order traversal after deletion of", val)
    aTree.preOrder()
    print()
    
    val = 16
    aTree.delete( val )

    print( aTree )
   
        

