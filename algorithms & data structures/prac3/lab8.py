class Node:
    def __init__(self, item, nex=None, prev=None):
        '''
        the node class for the double linked list where each item in the list is a node linked with the previous and the following
        @param item: any item type
        @param nex: the address of the next node
        @param prev: the address of the prev node
        @return: instance of this class
        @complexity: O(1)
        '''
        self.item = item
        self.nex = nex
        self.prev = prev

class DLList:
    def __init__(self):
        '''
        initialize the Double Linked List instance
        :return: an instance of this class
        :complexity: O(1)
        '''
        self.length = 0
        self.head = None

    def is_empty(self):
        '''
        returns whether the length of the list is 0
        :return: boolean
        :complexity: O(1)
        '''
        return self.length == 0

    def reset(self):
        '''
        restores the list to its initial state
        :post: head is set to none and length is set to zero
        :complexity: O(1)
        '''
        self.__init__()

    def __len__(self):
        '''
        returns the length of the list
        :return: integer, positive
        :complexity: O(1)
        '''
        return self.length

    def _getNode(self, index):
        '''
        finds node corresponding to index
        :param: index, integer in range of length of list
        :return: address of node 
        :complexity: O(N), where N = index
        '''
        if index < 0 or index >= len(self):
            raise IndexError

        node = self.head

        for _ in range(index):
            node = node.nex

        return node

    def append(self, item):
        '''
        appends a new item at the end of the list
        :param item: any object type
        :complexity: O(N)
        '''
        if self.is_empty():
            self.head = Node(item)
        else:
            current = self.head
            while current.nex != None:
                current = current.nex
            current.nex = Node(item)
        self.length += 1

    def insert(self, item, num):
        '''
        inserts an item BEFORE the given index, so after insertion the item's index = given index
        :param item: any object type
        :param num: integer representing index
        :complexity: O(N), where N = index
        '''
        try:
            index = self.get_index(num)
        except TypeError:
            raise TypeError("Index must be an integer")

        if index < 0:
            index = 0
        elif index > len(self):
            index = len(self)

        if index == 0:
            self.head = Node(item, self.head)
            if self.head.nex is not None:
                self.head.nex.prev = self.head
        else:
            node = self._getNode(index-1)
            node.nex = Node(item, node.nex, node)
            if node.nex.nex is not None:
                node.nex.nex.prev = node.nex

        self.length += 1

    def get_index(self, i):           
    # handles negative i like python
        '''
        returns the 'actual' index of the given index based on list's length
        :param i: integer
        :return: an integer between 0 and length
        :complexity: O(1)
        '''
        try:
            i = int(i)
        except ValueError:
            raise TypeError
        if i < 0:
            return i + len(self)
        else:
            return i

    def delete(self, num=None):
        '''
        deletes line of text at position num or all lines if no num is given
        :param num: integer, optional
        :complexity: O(1) best (delete all lines), O(N) worst
        '''
        if num == '':
            num = None

        if num != None:
            try:
                index = self.get_index(num)
            except TypeError:
                raise TypeError("Index must be an integer")
            if self.is_empty():
                raise IndexError("No items in list")
            if index >= len(self) or index < 0:
                raise IndexError("Index out of range")
            
            if index == 0:
                self.head = self.head.nex
                if self.head is not None:
                    self.head.prev = None
            else:
                node = self._getNode(index-1)
                node.nex = node.nex.nex
                if node.nex is not None:
                    node.nex.prev = node
            self.length -= 1

        elif num == None:
            self.reset()

    def __str__(self, num=None):
        if num is None:
            string = ''
            current = self.head
            while current is not None:
                string += str(current.item)
                current = current.nex
        else:
            try:
                index = self.get_index(num)
            except TypeError:
                raise TypeError("Index must be an integer")
            if index >= len(self) or index < 0:
                raise IndexError("Index out of range")
            node = self._getNode(index)
            string =  str(node.item)
        
        return string

    def __print__(self, num=None):
        '''
        returns the string of the list's element at position num or if no num is given, returns a string of all the elements
        :param num: None OR integer between -length and length-1
        :return: string
        :complexity: O(length) worse, O(num) best
        '''
        if num == '':
            num = None
        
        print(self.__str__(num))

class OrderedStack:
    def __init__(self):
        self.list = DLList()

    def __len__(self):
        """
        @pre none
        @post returns amount of items in stack
        @complexity best = worse = O(1)
        """
        return len(self.list)

    def is_empty(self):
        '''
        returns True if stack has nothing in it or False otherwise
        @ return: Boolean
        @ pre:  object of this class
        @ complexity: O(1)
        '''
        return self.list.is_empty()

    def __str__(self):
        """
        @param the stack itself
        @pre none
        @post string with items in stack separated 
            by spaces and starting from the one at the top
        @complexity best = worse = O(N)
        """
        a_string = ""
        current = self.list.head
        while current is not None:
            a_string += str(current.item)
            if current.nex is not None:
                a_string += " "
            current = current.nex
        return a_string

    def peek(self):
        '''
        returns the stack's top without popping it
        @ pre: object of this class
        @ post: None
        @ return: top
        @ complexity: O(1)
        '''
        assert not self.is_empty(), "Stack is empty"

        return self.list.head.item

    def pop(self):
        '''
        returns the value of the Stack's top and delete that item
        @ return: top
        @ pre: Object of this class, and stack not empty
        @ post: stack's length reduced by 1, stack's top becomes the next item
        @ complexity: O(1)
        '''
        assert not self.is_empty(), "Stack is empty"

        item = self.list.head.item
        self.list.delete(0)

        return item

    def push(self, item):
        '''
        pushes an item into the stack
        @ complexity: O(N)
        '''
        self.list.insert(item, 0)
        current = self.list.head
        while current.nex is not None and current.nex.item > item:
            self.list.delete(1)

    def destroy(self):
        while not self.is_empty():
            self.pop()

def menu():
    quit = False
    the_stack = OrderedStack()
    while not quit:
        commands = [0, 1, 2, 3, 4, 5, 6, 7]
        print(
            '''
            ---Linked List class menu---
            Available commands:
            1. is_empty
            2. print
            3. length
            4. peek
            5. pop
            6. push
            7. destroy
            0. quit
            '''
            )
        try:
            command = int(input('Input command: '))
        except TypeError:
            print('Command not an integer, try again')
        else:
            try:
                assert command in commands
            except AssertionError:
                print('Unknown command, try again')
            else:
                if command == 1:
                    print(the_stack.is_empty())
                elif command == 2:
                    print(str(the_stack))
                elif command == 3:
                    print(len(the_stack))
                elif command == 4:
                    print(the_stack.peek())
                elif command == 5:
                    print("stack before: " + str(the_stack))
                    print(the_stack.pop())
                    print("stack after: " + str(the_stack))
                elif command == 6:
                    item = input("item to push: ")
                    print("stack before: " + str(the_stack))
                    the_stack.push(item)
                    print("stack after: " + str(the_stack))
                elif command == 7:
                    the_stack.destroy()
                    print(str(the_stack))
                elif command == 0:
                    quit = True

# if __name__ == '__main__':
#     menu()


# l = DLList()
# l.insert(4,0)
# l.insert(0,0)
# print(str(l))
# print(l.head.nex.item)
# print(l.head.nex.prev.item)

# s = OrderedStack()
# s.push(4)
# print(str(s))
# s.push(3)
# print(str(s))

def read_file(fname):
    f = open(fname, 'r')
    lines = [line.rstrip('\n') for line in f]
    f.close()
    for i in range(1,len(lines)):
        lines[i] = lines[i].split(' ')
    return lines

class DisjointSets():
    def __init__(self, amount):
        self.array = [-1]*(amount+1)

    def union(self, set1, set2, nodes_visited):
        set1, nodes_visited = self.find(set1, nodes_visited)
        set2, nodes_visited = self.find(set2, nodes_visited)
        assert set1 != set2
        if self.array[set1] < self.array[set2] or (self.array[set1] == self.array[set2] and set1 < set2):
            # set1 is gonna be root
            self.array[set1] = self.array[set1] + self.array[set2]
            self.array[set2] = set1
        else:
            # set2 is gonna be root
            self.array[set2] = self.array[set1] + self.array[set2]
            self.array[set1] = set2
        return nodes_visited

    def find(self, set1, nodes_visited):
        while self.array[set1] >= 0:
            set1 = self.array[set1]
            nodes_visited += 1
        return set1, nodes_visited

    def findWithComp(self, set1, nodes_visited):
        updates = []
        while self.array[set1] >= 0:
            updates.append(set1)
            set1 = self.array[set1]
            nodes_visited += 1

        for set2 in updates:
            self.array[set2] = set1
        
        return set1, nodes_visited

def task3():
    lines = read_file("input.txt")
    ds = DisjointSets(int(lines[0]))
    nodes_visited = 0
    for i in range(1, len(lines)):
        if(lines[i][0] == "union"):
            nodes_visited = ds.union(int(lines[i][1]),int(lines[i][2]), nodes_visited)
        elif(lines[i][0] == "find"):
            print(ds.array)
            root, nodes_visited = ds.find(int(lines[i][1]),nodes_visited)
    print("without compression: " + str(nodes_visited))
    print("\n")
    ds = DisjointSets(int(lines[0]))
    nodes_visited = 0
    for i in range(1, len(lines)):
        if(lines[i][0] == "union"):
            nodes_visited = ds.union(int(lines[i][1]),int(lines[i][2]), nodes_visited)
        elif(lines[i][0] == "find"):
            root, nodes_visited = ds.findWithComp(int(lines[i][1]),nodes_visited)
    print("with compression: " + str(nodes_visited))

task3()