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

'''
1. 
    - edges are not directed, given that can fly in both 
        directions with same cost (so it's not a DAG)
    - finding cheapest route is a matter of finding path 
        with smallest weight(cost)
    - BFS doesn't take weight in consideration
    - possibilities:
        - Dijkstra
            - complexity = O(|E|*log|V|)
        - Bellman-Ford
            - complexity = O(|E|*|V|)

    given that weights will not be negative, it is unnecessary 
    to use Bellman-Ford. Therefore, Dijkstra is the best 
    alternative, as it has a better worst case complexity 
    than Bellman-Ford
'''

'''
task2:
- graph is dictionary of vertices (keys are their names)
- each vertex is represented by a Vertex data type object
- Vertex data type holds information such as name and adj list
- adjacency list hold vertices to which Vertex is connected by edge
- items in adjacency list are of class node
- each node represents an edge, 
    and stores name and cost for the vertice to where it goes
'''

INF = 99999999999999

class Vertex:
    def __init__(self, name):
        self.adj = LList()
        self.known = False
        self.path = None
        self.dist = INF
        self.name = name

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

    def bellmanFord(self, s):
        for v in self.vertices.values():
            v.dist = INF
            v.known = False
        s.dist = 0

        for i in range(1, self.amountV()):
            for v in self.vertices.values():
                for i in range(len(v.adj)):
                    u = v.adj.getItem(i).item
                    if v.dist > u.dist + self.cost(u,v):
                        v.dist = u.dist + self.cost(u,v)
                        v.path = u

    def bipartite(self):
        a = {}
        b = {}
        Q = LinkedQueue();
        for v in self.vertices.values():
            Q.append(v)
            a[v] = v.name
            break
        while not Q.is_empty():
            v = Q.serve()
            try:
                a[v]
                for i in range(len(v.adj)):
                    u = v.adj.getItem(i).item
                    try:
                        a[u]
                        return False
                    except KeyError:
                        try:
                            b[u]
                        except KeyError:
                            b[u] = u.name
                            Q.append(u)
            except KeyError:
                b[v] = v.name
                for i in range(len(v.adj)):
                    u = v.adj.getItem(i).item
                    try:
                        b[u]
                        return False
                    except KeyError:
                        try:
                            a[u]
                        except KeyError:
                            a[u] = u.name
                            Q.append(u)
        return True

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

def task2():
    g = initializeGraph("input.txt")
    g.printInfo()

def task3(start, end):
    g = initializeGraph("input.txt")
    s = g.getVertex(start)
    g.dijkstra(s)
    current = g.getVertex(end)
    cost = current.dist
    path = current.name
    while current.path is not None:
        path = current.path.name + ", " + path
        current = current.path
    print(path, end=", $")
    print(cost)

def bf(start, end):
    g = initializeGraph("input.txt")
    s = g.getVertex(start)
    g.bellmanFord(s)
    current = g.getVertex(end)
    cost = current.dist
    path = current.name
    while current.path is not None:
        path = current.path.name + ", " + path
        current = current.path
    print(path, end=", $")
    print(cost)

def bi():
    g = Graph()
    g.addVertex("v1")
    g.addVertex("v2")
    g.addEdge("v1", "v2", 1)
    g.addVertex("v3")
    g.addVertex("v2")
    g.addEdge("v3", "v2", 1)
    if g.bipartite():
        print("bipartite")
    else:
        print("not bipartite")


'''
task4:
    BFS would be the most efficient algorithm
        - given that we might be interested in more expensive
        paths, the weight of the path is not a decisive factor
modifications: update the costs; 
doesnt'only change distace if it's set to infinity
'''

def task5(start, end):
    g = initializeGraph("input.txt")
    s = g.getVertex(start)
    g.modifiedBFS(s)
    end = g.getVertex(end)
    for i in range(len(end.dist)):
        current = end
        path = end.name
        cost = end.dist[i][0]
        j = i
        while current.dist[j][2] is not None:
            path = current.dist[j][2].name + ", " + path
            edges = current.dist[j][1]
            current = current.dist[j][2]
            for j in range(edges):
                if current.dist[j][1] == edges - 1:
                    break
        if current == s:
            print(path, end=", $")
            print(cost)        

task2()
# city1 = str(input("Start city: "))
# city2 = str(input("End city: "))
city1 = "Melbourne" 
city2 = "Brisbane"
print("Task 3:")
task3(city1, city2)
print("------------------------------------")
print("Bellman-Ford:")
bf(city1, city2)
print("------------------------------------")
print("Task 5:")
task5(city1, city2)
bi()


'''
task 6

vertex |     |     |   |   |
A      |  0  |  0  | 0 | 0 |
B      | INF |  1  | 1 | 1 |
C      | INF |  3  | 2 | 2 |
D      | INF |  2  | 2 | 2 |
E      | INF | INF | 5 | 0 |
F      | INF | INF | 3 | 3 |

'''