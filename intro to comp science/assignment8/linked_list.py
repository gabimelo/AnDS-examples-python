"""
@author Brian Ezra, Gabriela Melo
@since 11/05/2015
@modified 15/05/2015
"""

class Node:
    def __init__(self, item, link=None):
        '''
        the node class for the licked list where each item in the list is a node linked with another
        :param item: any item type
        :param link: the address of the next node
        :return: tan instance of this class
        :complexity: O(1)
        '''
        self.item = item
        self.link = link


class LList:
    def __init__(self):
        '''
        initialize the Linked List instance
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

    def is_full(self):
        '''
        returns False, if memory is full, system will return an exception
        :return: False
        :complexity: O(1)
        '''
        return False

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
            node = node.link

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
            while current.link != None:
                current = current.link
            current.link = Node(item)
        self.length += 1

    def insert(self, item, num):
        '''
        inserts an item BEFORE the given index, so after insertion the item's index = given index
        :param item: any object type
        :param num: integer
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
        else:
            node = self._getNode(index-1)
            node.link = Node(item, node.link)

        self.length += 1

    def get_index(self, i):           # handles negative i like python
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
                self.head = self.head.link
            else:
                node = self._getNode(index-1)
                node.link = node.link.link
            self.length -= 1

        elif num == None:
            self.reset()

    def __str__(self, num=None):
        if num is None:
            string = ''
            current = self.head
            while current is not None:
                string += str(current.item)
                current = current.link
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

def menu():
    '''
    a menu to test the linked list class
    :return: None
    '''
    quit = False
    the_list = LList()
    while not quit:
        commands = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(
            '''
            ---Linked List class menu---
            Available commands:
            1. is_empty
            2. is_full
            3. length
            4. append
            5. insert
            6. delete
            7. get index
            8. print
            9. reset
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
                    print(the_list.is_empty())
                elif command == 2:
                    print(the_list.is_full())
                elif command == 3:
                    print(len(the_list))
                elif command == 4:
                    item = input('Input item to be appended: ')
                    the_list.append(item)
                elif command == 5:
                    item = input('Input item to be inserted: ')
                    i = input('Insert index: ')
                    try:
                        the_list.insert(item, i)
                    except TypeError:
                        print('Index must be an integer')
                elif command == 6:
                    print('Available index:')
                    for j in range(the_list.__len__()):
                        print(j, end=' ')
                    i = input('\nInput index of item to be deleted(can be None): ')
                    
                    if i =='':
                        i = None
                    try:
                        the_list.delete(i)
                    except IndexError:
                        print('Index out of range')
                    except TypeError:
                        print('Index must be an integer')
                elif command == 7:
                    try:
                        i = int(input('Insert index: '))
                    except TypeError:
                        print('Index not integer')
                    print(the_list.get_index(i))
                elif command == 8:
                    i = input('Input index(can be empty): ')
                    if i == '':
                        the_list.__print__()
                    else:
                        try:
                            the_list.__print__(i)
                        except (IndexError, TypeError):
                            print('Invalid index')
                elif command == 9:
                    the_list.reset()
                elif command == 0:
                    quit = True

if __name__ == '__main__':
    menu()
