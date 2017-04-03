class Node:
    def __init__(self, item, cost=0, link=None, flow = None, cap = None):
        '''
        the node class for the licked list where each item in the list is a node linked with another
        :param item: any item type
        :param link: the address of the next node
        :return: tan instance of this class
        :complexity: O(1)
        '''
        self.item = item
        self.link = link
        self.cost = cost
        self.flow = flow
        self.capacity = cap

class LList:
    def __init__(self):
        '''
        initialize the Linked List instance
        :return: an instance of this class
        :complexity: O(1)
        '''
        self.length = 0
        self.head = None

    def index(self, item):
        'returns -1 if item is not in list, else returns index'
        current = self.head
        i = 0
        while current is not None:
            if current.item == item:
                return i
            current = current.link
            i+=1
        return -1

    def getItem(self, index):
        current = self.head
        for i in range(index):
            assert current is not None, "index out of range"
            current = current.link
        return current

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

    def append(self, item, cost, cap):
        '''
        appends a new item at the end of the list
        :param item: any object type
        :complexity: O(N)
        '''
        if self.is_empty():
            self.head = Node(item, cost, None, None, cap)
        else:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = Node(item, cost, None, None, cap)
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

class minHeap:
    def __init__(self):
        self.count = 0
        self.array = [None]

    def is_empty(self):
        return self.count == 0

    def buildHeap(self, a):
        self.count = len(a)
        for item in a:
            self.array.append(item)
        i = self.count//2
        while i > 0:
            self.percolateDown(i)
            i -= 1

    def percolateDown(self, i):
        while i*2 <= self.count:
            child = self.get_smallest_child(i)
            if self.array[child].dist > self.array[i].dist:
                break
            self.swap(child, i)
            i = child

    def get_smallest_child(self, i):
        try:
            assert (i*2+1)<=self.count
        except AssertionError:
            return i*2
        if self.array[i*2].dist < self.array[i*2+1].dist:
            return i*2
        else:
            return i*2+1

    def swap(self, pos1, pos2):
        temp = self.array[pos1]
        self.array[pos1] = self.array[pos2]
        self.array[pos2] = temp

    def __str__(self):
        s = ""
        for i in range(1, len(self.array)):
            s += self.array[i].name
            s += " "
        return s

    def removeMin(self):
        assert not self.is_empty(), "Can't serve from empty list"
        item = self.array[1]
        self.swap(1, self.count)
        self.count -= 1

        self.percolateDown(1)
        return item

    def decreaseKey(self, v):
        i = 1
        while self.array[i] != v:
            i += 1
        self.percolateUp(i)

    def percolateUp(self, k):
        while k//2 > 0:
            if self.array[k].dist >= self.array[k//2].dist:
                break
            self.swap(k, k//2)
            k = k//2

class LinkedQueue:
    def __init__(self):
        self.rear = None
        self.front = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def reset(self):
        self.rear = None
        self.front = None
    
    def append(self, item):
        node = Node(item)

        if self.is_empty():
            self.front = node
        else:
            self.rear.link = node

        self.rear = node

    def serve(self):
        assert not self.is_empty(), "Queue is empty"

        item = self.front.item
        self.front = self.front.link

        if self.is_empty():
            self.rear = None

        return item

INF = 99999999999999

class Vertex:
    def __init__(self, name):
        self.adj = LList()
        self.known = False
        self.path = None
        self.dist = INF
        self.name = name
        self.indegree = 0

class Graph:
    def __init__(self):
        self.vertices = {}

    def amountV(self):
        return len(self.vertices)
   
    def addVertex(self, name):
        try:
            self.vertices[name]
        except KeyError:
            self.vertices[name] = Vertex(name)

    def getVertex(self, name):
        try:
            return self.vertices[name]
        except KeyError:
            print("Vertex not found")

    def addEdge(self, v1, v2, cost, cap=None):
        # this is for directed edges only
        try:
            self.vertices[v1].adj.append(self.vertices[v2], cost, cap)
        except KeyError:
            print("One or more vertices could not be found in graph")

    def deleteEdge(self, v1, v2):
        # v1 and v2 are the names of vertices
        try:
            v1 = self.vertices[v1]
        except KeyError:
            print("Vertex v1 could not be found in graph")
            return
        for i in range(len(v1.adj)):
            e = v1.adj.getItem(i)
            if e.item.name == v2:
                v1.adj.delete(i)
                break

    def updateEdgeFlow(self, v1, v2, flow, add = False):
        # v1 and v2 are the names of vertices
        try:
            v1 = self.vertices[v1]
        except KeyError:
            print("Vertex v1 could not be found in graph")
            return
        for i in range(len(v1.adj)):
            e = v1.adj.getItem(i)
            if e.item.name == v2:
                if add:
                    e.flow += flow
                    if e.flow == 0:
                        self.deleteEdge(v1.name,v2)
                else:
                    e.flow =  flow
                break

    def printInfo(self, dist=False):
        for v in self.vertices.values():
            print("Edges from "+str(v.name)+":")
            if dist:
                    print("dist of this edge: " + str(v.dist))
            for i in range(len(v.adj)):
                e = v.adj.getItem(i)
                print(e.flow, end=": ")
                print(v.name,end=" ---> ")
                print(e.item.name)
            print("------------------------------------")

    def cost(self, v, u):
        cost = -1
        for i in range(len(v.adj)):
            e = v.adj.getItem(i)
            if e.item.name == u.name:
                cost =  e.cost
                break
        return cost

    def flow(self, v, u):
        flow = -1
        for i in range(len(v.adj)):
            e = v.adj.getItem(i)
            if e.item.name == u.name:
                flow =  e.flow
                break
        return flow

    def topSort(self):
        Q = LinkedQueue()
        out = LinkedQueue()

        for v in self.vertices.values():
            v.indegree = 0
        for v in self.vertices.values():
            for i in range(len(v.adj)):
                w = v.adj.getItem(i).item
                w.indegree += 1

        for v in self.vertices.values():
            if v.indegree == 0:
                Q.append(v)

        while not Q.is_empty():
            v = Q.serve()
            out.append(v)
            for i in range(len(v.adj)):
                w = v.adj.getItem(i).item
                w.indegree -= 1
                if w.indegree == 0:
                    Q.append(w)
        return out            

    def dagShortest(self, s):
        for v in self.vertices.values():
            v.dist = INF
            v.path = None
        s.dist = 0
        Q = self.topSort()
        while not Q.is_empty(): # |V|
            v = Q.serve()
            for i in range(len(v.adj)): # |E|
                u = v.adj.getItem(i).item
                if u.dist > v.dist + self.cost(v, u):
                    u.dist = v.dist + self.cost(v, u)
                    u.path = v

    def buildResidual(self):
        Gr = Graph ()
        for v in self.vertices.values():
            Gr.addVertex(v.name)
        for v in self.vertices.values():
            for i in range(len(v.adj)):
                e = v.adj.getItem(i)
                w = e.item
                Gr.addEdge(v.name,w.name, 0)
                Gr.updateEdgeFlow(v.name,w.name, e.capacity)
        return Gr

    def updateAllEdgesFlow(self, flow):
        for v in self.vertices.values():
            for i in range(len(v.adj)):
                w = v.adj.getItem(i).item
                self.updateEdgeFlow(v.name,w.name,flow)

def augmentingPath(g, s, t):
    # s and t are the names of the vertices
    start = g.getVertex(s)
    g.dagShortest(start)
    current = g.getVertex(t)
    maxFlow = INF
    path = [current.name]
    while current.path is not None:
        maxFlow = min(maxFlow, g.flow(current.path, current))
        path.append(current.path.name)
        current = current.path
    if current.name == "s":
        return path, maxFlow 
    else:
        return False, False

def augmentFlow(g, Gr, flow, path):
    for i in range(len(path)-1):
        g.updateEdgeFlow(path[i+1], path[i], flow, True)
        Gr.updateEdgeFlow(path[i+1], path[i], -flow, True)

def FordFulkerson(g, s, t):
    # s and t are the names of the vertices
    g.updateAllEdgesFlow(0)
    Gr = g.buildResidual()
    path, maxFlow = augmentingPath(Gr, s, t)
    while path:
        augmentFlow(g, Gr, maxFlow, path)
        path, maxFlow = augmentingPath(Gr, s, t)

g = Graph()
g.addVertex("s")
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("t")
g.addEdge("s", "A", 0, 4)
g.addEdge("s", "B", 0, 5)
g.addEdge("s", "C", 0, 5)
g.addEdge("A", "D", 0, 8)
g.addEdge("B", "D", 0, 5)
g.addEdge("B", "t", 0, 3)
g.addEdge("C", "B", 0, 2)
g.addEdge("C", "t", 0, 3)
g.addEdge("D", "t", 0, 7)
FordFulkerson(g,"s", "t")
g.printInfo()