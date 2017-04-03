class Node:
    def __init__(self, item, cost=0, link=None):
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

    def append(self, item, cost):
        '''
        appends a new item at the end of the list
        :param item: any object type
        :complexity: O(N)
        '''
        if self.is_empty():
            self.head = Node(item, cost)
        else:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = Node(item, cost)
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

    def __len__(self):
        return self.count

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

class minHeapEdges:
    def __init__(self):
        self.count = 0
        self.array = [None]

    def is_empty(self):
        return self.count == 0

    def __len__(self):
        return self.count

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
            if self.array[child].cost > self.array[i].cost:
                break
            self.swap(child, i)
            i = child

    def get_smallest_child(self, i):
        try:
            assert (i*2+1)<=self.count
        except AssertionError:
            return i*2
        if self.array[i*2].cost < self.array[i*2+1].cost:
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
            if self.array[k].cost >= self.array[k//2].cost:
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

class DisjointSets():
    def __init__(self, amount):
        self.array = [-1]*(amount+1)

    def union(self, set1, set2):
        set1 = self.find(set1)
        set2 = self.find(set2)
        assert set1 != set2
        if self.array[set1] < self.array[set2] or (self.array[set1] == self.array[set2] and set1 < set2):
            # set1 is gonna be root
            self.array[set1] = self.array[set1] + self.array[set2]
            self.array[set2] = set1
        else:
            # set2 is gonna be root
            self.array[set2] = self.array[set1] + self.array[set2]
            self.array[set1] = set2

    # def find(self, set1, nodes_visited):
    #     while self.array[set1] >= 0:
    #         set1 = self.array[set1]
    #         nodes_visited += 1
    #     return set1, nodes_visited

    def find(self, set1):
        updates = []
        while self.array[set1] >= 0:
            updates.append(set1)
            set1 = self.array[set1]

        for set2 in updates:
            self.array[set2] = set1
        
        return set1

INF = 99999999999999

class Vertex:
    def __init__(self, name):
        self.adj = LList()
        self.known = False
        self.path = None
        self.dist = INF
        self.name = name

class Edge:
    def __init__(self, v1, v2, cost):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost

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

    def addEdge(self, v1, v2, cost):
        # this is for undirected edges only
        try:
            self.vertices[v1].adj.append(self.vertices[v2], cost)
            self.vertices[v2].adj.append(self.vertices[v1], cost)
        except KeyError:
            print("One or more vertices could not be found in graph")

    def printInfo(self):
        for v in self.vertices.values():
            print("Flights from "+str(v.name)+":")
            for i in range(len(v.adj)):
                e = v.adj.getItem(i)
                print(e.cost, end=": ")
                print(v.name,end=" ---> ")
                print(e.item.name)
            print("------------------------------------")

    def cost(self, u, v):
        cost = -1
        for i in range(len(v.adj)):
            e = v.adj.getItem(i)
            if e.item.name == u.name:
                cost =  e.cost
                break
        return cost

    def dijkstra(self, s):
        for v in self.vertices.values():
            v.dist = INF
            v.known = False
        s.dist = 0

        heap = minHeap()
        heap.buildHeap(self.vertices.values())
        while not heap.is_empty():
            u = heap.removeMin()
            u.known = True
            for i in range(len(u.adj)):
                v = u.adj.getItem(i).item
                if v.known == False and v.dist > u.dist + self.cost(u,v):
                    v.dist = u.dist + self.cost(u,v)
                    heap.decreaseKey(v)
                    v.path = u

    def modifiedBFS(self, s):
        Q = LinkedQueue()
        for v in self.vertices.values():
            v.dist = []
            v.dist.append([INF,INF,None])
            # each item in v.dist is [sum of cost][edges][path]
            v.known = False
        s.dist[0]=[0,0,None]
        Q.append(s)
        while not Q.is_empty(): # |V|
            v = Q.serve()
            v.known = True
            for path in range(len(v.dist)): # amount of different paths
                for i in range(len(v.adj)): # |E|
                    w = v.adj.getItem(i).item
                    if w.known == False:
                        if w.dist[0][0] == INF:
                            Q.append(w)
                        costvw = self.cost(v,w)
                        if w.dist[0][0] > v.dist[path][0]+costvw: # there is a cheaper path
                            # add at position relative to amount of stops
                            i = 0
                            while i<len(w.dist) and w.dist[i][1] < v.dist[path][1]+1:
                                i+=1
                            w.dist.insert(i,[v.dist[path][0]+costvw, v.dist[path][1]+1, v])
                            if w.dist[i][1] == w.dist[i+1][1]:
                                w.dist.pop(i+1)
                        elif w.dist[0][1] > v.dist[path][1]+1: # there is a path with less stops
                            #add at beginning
                            w.dist.insert(0,[v.dist[path][0]+costvw, v.dist[path][1]+1, v])

    def FloydWarshall(self):
        D = []
        count = 0
        for i in self.vertices.values():
            tmp = []
            print(str(count) + " " + i.name)
            for j in self.vertices.values():
                found = False
                for k in range(len(i.adj)): # |E|
                    w = i.adj.getItem(k)
                    if w.item == j:
                        found = w
                        break
                if found:
                    tmp.append(found.cost)
                else:
                    tmp.append(INF)
            D.append(tmp)
            count += 1
        n = self.amountV()
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if D[i][k]+D[k][j] < D[i][j]:
                        D[i][j] = D[i][k]+D[k][j]
        return D

    def prim(self, s):
        for v in self.vertices.values():
            v.dist = INF
        s.dist = 0

        heap = minHeap()
        heap.buildHeap(self.vertices.values())
        while not heap.is_empty():
            u = heap.removeMin()
            for i in range(len(u.adj)):
                v = u.adj.getItem(i).item
                if v.dist > self.cost(u,v):
                    v.dist = self.cost(u,v)
                    heap.decreaseKey(v)
                    v.path = u

    def printPrim(self):
        for v in self.vertices.values():
            print(v.name + " dist= " + str(v.dist))

    def kruskal(self):
        for v in self.vertices.values():
            v.known = False
        self.MST = []

        dic = {}
        a = []
        counter = 0
        for v1 in self.vertices.values():
            if not v1.known:
                for i in range(len(v1.adj)):
                    e = v1.adj.getItem(i)
                    v2 = e.item
                    if not v2.known:
                        cost = e.cost
                        a.append(Edge(v1,v2,cost))
                dic[v1] = counter
                v1.known = True
                counter+=1
        H = minHeapEdges()
        H.buildHeap(a)

        T = DisjointSets(len(H))
        while not H.is_empty():
            e = H.removeMin()
            v1 = e.v1
            v2 = e.v2
            try:
                T.union(dic[v1], dic[v2])
                self.MST.append(e)
            except AssertionError:
                pass

    def printKruskal(self):
        for item in self.MST:
            print("From " + item.v1.name + " to " + item.v2.name)

def read_file(fname):
    f = open(fname, 'r')
    lines = [line.rstrip('\n') for line in f]
    f.close()
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')
        temp = lines[i][0].split(',')
        lines[i][0] = temp[0]
        temp = lines[i][1].split(',')
        lines[i][1] = temp[0]
    return lines

def initializeGraph(fName):
    '''
    @pre: input file is exactly in specified format
    '''
    lines = read_file(fName)
    g = Graph()
    for line in lines:
        g.addVertex(line[0])
        g.addVertex(line[1])
        g.addEdge(line[0], line[1], int(line[2]))
    return g

class GraphMatrix:
    def __init__(self):
       self.vertices = []
       self.dict = {}

    def amountV(self):
        return len(self.vertices)
   
    def addVertex(self, name):
        try:
            self.dict[name]
        except KeyError:
            self.dict[name] = len(self.vertices)
            if len(self.vertices) != 0:
                self.vertices.append([INF]*(len(self.vertices[0])))
                for i in range(len(self.vertices)):
                    self.vertices[i].append(INF)
            else:
                self.vertices.append([INF])

    def getVertex(self, name):
        try:
            index = self.dict[name]
        except KeyError:
            print("Vertex not found")
        return self.vertices[index]

    def addEdge(self, v1, v2, cost):
        # this is for undirected edges only
        try:
            i1 = self.dict[v1]
            i2 = self.dict[v2]
        except KeyError:
            print("One or more vertices could not be found in graph")
        self.vertices[i1][i2] = cost
        self.vertices[i2][i1] = cost

    def printInfo(self):
        for k in self.dict.keys():
            print("Flights from " + str(k) + ":")
            for i in range(len(self.vertices[self.dict[k]])):
                if self.vertices[self.dict[k]][i] != INF:
                    for key, value in self.dict.items():
                        if value == i:
                            print(str(self.vertices[self.dict[k]][i]) + ": " + str(key))
            print("----------------------------")

    def cost(self, u, v):
        i1 = self.dict[u]
        i2 = self.dict[v]
        return self.vertices[i1][i2]

    def FloydWarshall(self):
        D = []
        for i in self.vertices:
            tmp = []
            for j in i:
                tmp.append(j)
            D.append(tmp)
        n = len(self.vertices)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if D[i][k]+D[k][j] < D[i][j]:
                        D[i][j] = D[i][k]+D[k][j]
        return D

def initializeGraphMatrix(fName):
    '''
    @pre: input file is exactly in specified format
    '''
    lines = read_file(fName)
    g = GraphMatrix()
    for line in lines:
        g.addVertex(line[0])
        g.addVertex(line[1])
        g.addEdge(line[0], line[1], int(line[2]))
    return g

def task1():
    g = initializeGraph("input.txt")
    g.printInfo()
    print("Shortest paths through Floyd-Warshall:")
    for item in g.FloydWarshall():
        print(item)
    print("----------------------------")

def task3():
    g = initializeGraph("input.txt")
    s = g.getVertex("Melbourne") # doesn't matter which one
    g.prim(s)
    print("Minimum Spanning Tree through Prim's Algorithm:", end="\n\n")
    g.printPrim()
    print("----------------------------")
    g = initializeGraph("input.txt")
    g.kruskal()
    print("Minimum Spanning Tree through Kruskal's Algorithm:", end="\n\n")
    g.printKruskal()
    print("----------------------------")

def task4(A):
    # first item is sum, second is starting index
    T = []
    T.append([1,0])
    for i in range(1,len(A)):
        if A[i] < A[i-1]:
            index = i
            sum = 1
        else:
            index = T[i-1][1]
            sum = 1 + T[i-1][0]
        T.append([sum, index])
    max = T[0][0]
    start = 0
    end = 0
    for i in range(1,len(T)):
        if T[i][0] > max:
            max = T[i][0]
            start = T[i][1]
            end = i
    return max, start, end

task1()
task3()
print(task4([3,10,-3,5,7]))