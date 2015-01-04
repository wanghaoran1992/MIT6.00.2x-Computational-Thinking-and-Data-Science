# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
from graph import *

#
# Problem 1: CREATING THE DATA STRUCTURE REPRESENTATION
#

class WeightedDigraph(Digraph):
    """
        Weighted directed graph derived from class Digraph
        """
    def __init__(self):
        Digraph.__init__(self)
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        tot = edge.getTotalDistance()
        outd = edge.getOutdoorDistance()
        if not(Node(src) in self.nodes and Node(dest) in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest, (tot, outd)])
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2} ({3}, {4})\n'.format(res, k, d[0], float(d[1][0]), float(d[1][1]))
        return res[:-1]
    def childrenOf(self, node):
        res = []
        for d in self.edges[node]:
            res.append(d[0])
        return res

class WeightedEdge(Edge):
    def __init__(self, src, dest, tot, outd):
        if tot<outd:
            raise ValueError('Outdoor distance must be less than or equal to the total distance')
        Edge.__init__(self, src, dest)
        self.tot = tot
        self.outd = outd
    def getTotalDistance(self):
        return self.tot
    def getOutdoorDistance(self):
        return self.outd
    def __str__(self):
        return str(Edge.__str__(self) + ' (' + str(self.tot) + ', ' + str(self.outd) + ')')

#
# Problem 2: Building up the Campus Map
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    
    print "Loading map from file..."
        

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

# Helper Code

def DFS2(graph, start, end, q = []):
    ans=[]
    initPath = [start]
    q.append(initPath)
    while len(q) != 0:
        tmpPath = q.pop(0)
        lastNode = tmpPath[-1]
        ## print 'Current dequeued path:', printPath(tmpPath)
        if lastNode == end:
            ans.append(tmpPath)
            continue
        qt=[]
        for linkNode in graph.childrenOf(lastNode):
            if linkNode not in tmpPath:
                newPath = tmpPath + [linkNode]
                qt.append(newPath)
        ## q[:0]=qt
    q.extend(qt)

                    return ans



##def testSP(st,end):
## mitMap = load_map("mit_map.txt")
##
## ssp = DFS2(mitMap, mitMap.retNode(str(st)), mitMap.retNode(str(end)))
## for ind,sp in enumerate(ssp):
## print '#{} path found by DFS:'.format(ind), printPath(sp)

def getdis(digraph, path):
    edges=digraph.edges
    ts=[0,0]
    for start,end in zip(path[0:-1],path[1:]):
        for edge in edges[start]:
            if edge[0]==end:
                ts[0]=ts[0]+float(edge[1][0])
                ts[1]+=float(edge[1][1])
    return ts

def memoize(f):
    def memf(*x):
        y=(tuple(i) for i in x)
        
        if y not in memf.cache:
            memf.cache[y]=f(*x)
        return memf.cache[y]
    memf.cache = {}
    return memf

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    ssp = DFS2(digraph, digraph.retNode(str(start)), digraph.retNode(str(end)))
    pl=[]
    for sp in ssp:
        
        tdist=getdis(digraph, sp)
        if (tdist[0]<maxTotalDist and tdist[1]<maxDistOutdoors):
            pl.append([sp,tdist[0]])
    if pl==[]:
        raise ValueError
    minl=pl[0]
    for ll in pl:
        if ll[1]<minl[1]:
            minl=ll
    ans2=[str(ii) for ii in minl[0]]
    return ans2

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    stack = [Path([Node(start)], 0, 0)]
    
    while stack:
        path = stack.pop(-1)
        
        for edge in digraph.childrenOf(path.get_current_position()):
            if not path.is_node_visited(edge.getDestination()):
                new_path = path.clone()
                new_path.add_edge(edge)
                if (new_path.distance_outdoors <= maxDistOutdoors and
                    new_path.total_distance <= maxTotalDist):
                    if new_path.is_end_reached(end):
                        return new_path.get_node_list()
                    else:
                        stack.append(new_path)

    raise ValueError()


