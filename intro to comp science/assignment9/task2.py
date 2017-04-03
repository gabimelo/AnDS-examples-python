'''
@ author: Brian Ezra, Gabriela Melo
@ since: 15/05/2015
@ modified: 22/05/2015
'''

class TreeNode:
    def __init__(self , item , left , right):
        '''
        initialize the instance of this class
        :param item: object of any type
        :param left: address of left child
        :param right: address of right child
        :return: instance of this class
        :complexity: O(1)
        '''
        self.item = item
        self.right = right
        self.left = left

class BinaryTree:
    def __init__(self):
        '''
        initializes the instance of this class
        :return: an instance of this class
        :complexity: O(1)
        '''
        self.root = None

    def add(self , item , binary_str):
        '''
        appends and item at one of the tree branches based on the binary string argument
        :param item: object of any type
        :param binary_str: a binary string
        :return: none
        :complexity: O(len of binary_str)
        '''
        binary_str_itr = iter(binary_str)
        self.root = self.add_aux(self.root , item , binary_str_itr)

    def add_aux(self , current , item , binary_str_itr):
        '''
        the auxiliary method of add
        :param current: the current tree node it's pointing at
        :param item: the item to be added
        :param binary_str_itr: the iterator instance of binary_str
        :complexity: O(len of binary_str)
        '''
        if current is None:
            current = TreeNode(None , None , None)
        try:
            bit = next(binary_str_itr)
            if bit == '0':
                current.left = self.add_aux(current.left , item , binary_str_itr)
            elif bit == '1':
                current.right = self.add_aux(current.right , item , binary_str_itr)
        except StopIteration:
            current.item = item

        return current
    
    def get(self, binary_str):
        '''
        returns the item located at the binary_str
        :param binary_str: a binary string that determines an object's location within the tree
        :return: the item located at binary_str
        :complexity: O(length of binary_str)
        '''
        current = self.root
        for i in binary_str:
            if i == '0':
                current = current.left
            elif i == '1':
                current = current.right
            assert current is not None, "Invalid binary_str"
        return current.item

    def inorder_str(self):
        '''
        prints all the items in the tree using inorder notation
        :return: returns all the items on the tree as a string
        :complexity: O(num of items on tree)
        '''
        return self.inorder_str_aux(self.root, '')

    def inorder_str_aux(self, current, string):
        '''
        the auxiliary method of inorder_str
        :param current: the current node it's pointing at
        :param string: the string o be returned
        :return: string of all the items on the tree
        :complexity: O(num of items)
        '''
        if current.left is not None:
            string = self.inorder_str_aux(current.left,string)
        
        string += str(current.item)

        if current.right is not None:
            string = self.inorder_str_aux(current.right,string)

        return string

def menu():
    '''
    
    '''
    quit = False
    tree = BinaryTree()
    while not quit:
        commands = ['a', 'g', 'p', 'q', 'h']
        string = input('Enter command: ')
        command = string.split(' ')[0]
        try:
            op1 = string.split(' ')[1]
        except IndexError:
            op1 = None
        try:
            op2 = string.split(' ')[2]
        except IndexError:
            op2 = None
        try:
            assert command in commands
        except AssertionError:
            print('Unknown command, try again')
        else:
            if command == 'h':
                print(
                '''
                ---Binary Tree Class menu---
                Available commands:
                a     add item binary_str
                g 	get binary_str
                p 	print
                q 	quit
                '''
                )
            elif command == 'a':
                tree.add(op1, op2)
            elif command == 'g':
                tree.get(op2)
            elif command == 'p':
                print(tree.inorder_str())
            elif command == 'q':
                quit = True

# menu()