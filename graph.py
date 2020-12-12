"""
The polar expedition graph!
===========================

Contains the graph connecting the vertices (or base stations) on the map.

This is going to be the main file that you are modifying. :)

Usage:
    Contains the graph, requires the connection to vertices and edges.
"""
import math

from vertex import Vertex
from edge import Edge
import numpy as np



# Define a "edge already exists" exception
# Don't need to modify me.
class EdgeAlreadyExists(Exception):
    """Raised when edge already exists in the graph"""
    def __init__(self, message):
        super().__init__(message)


class Graph:
    """
    Graph Class
    -----------

    Represents the graph of vertices, which is equivalent to the map of base
    stations for our polar expedition.

    Attributes:
        * vertices (list): The list of vertices
    """

    def __init__(self):
        """
        Initialises an empty graph
        """
        self._vertices = []

    def insert_vertex(self, x_pos, y_pos):
        """
        Insert the vertex storing the y_pos and x_pos

        :param x_pos: The x position of the new vertex.
        :param y_pos: The y position of the new vertex.

        :type x_pos: float
        :type y_pos: float

        :return: The new vertex, also stored in the graph.
        """

        v = Vertex(x_pos, y_pos)
        self._vertices.append(v)
        return v

    def insert_edge(self, u, v):
        """
        Inserts the edge between vertex u and v.

        We're going to assume in this assignment that all vertices given to
        this will already exist in the graph.

        :param u: Vertex U
        :param v: Vertex V

        :type u: Vertex
        :type v: Vertex

        :return: The new edge between U and V.
        """

        e = Edge(u, v)

        # Check that the edge doesn't already exist
        for i in u.edges:
            if i == e:
                # Edge already exists.
                raise EdgeAlreadyExists("Edge already exists between vertex!")

        # Add the edge to both nodes.
        u.add_edge(e)
        v.add_edge(e)

    def remove_vertex(self, v):
        """
        Removes the vertex V from the graph.
        :param v:  The pointer to the vertex to remove
        :type v: Vertex
        """

        # Remove it from the list
        del self._vertices[self._vertices.index(v)]

        # Go through and remove all edges from that node.
        while len(v.edges) != 0:
            e = v.edges.pop()
            u = self.opposite(e, v)
            u.remove_edge(e)

    @staticmethod
    def distance(u, v):
        """
        Get the distance between vertex u and v.

        :param u: A vertex to get the distance between.
        :param v: A vertex to get the distance between.

        :type u: Vertex
        :type v: Vertex
        :return: The Euclidean distance between two vertices.
        """

        # Euclidean Distance
        # sqrt( (x2-x1)^2 + (y2-y1)^2 )

        return math.sqrt(((v.x_pos - u.x_pos)**2) + ((v.y_pos - u.y_pos)**2))

    @staticmethod
    def opposite(e, v):
        """
        Returns the vertex at the other end of v.
        :param e: The edge to get the other node.
        :param v: Vertex on the edge.
        :return: Vertex at the end of the edge, or None if error.
        """

        # It must be a vertex on the edge.
        if v not in (e.u, e.v):
            return None

        if v == e.u:
            return e.v

        return e.u

    ##############################################
    # Implement the functions below
    ##############################################

    def find_emergency_range(self, v):
        """
        Returns the distance to the vertex W that is furthest from V.
        :param v: The vertex to start at.
        :return: The distance of the vertex W furthest away from V.
        """
        # TODO implement me!
        furthest = 0
        for i in self._vertices:

            x = self.distance(v,i)

            if(x> furthest):
                furthest =x


        return round(furthest,5)




    def getNum(self,edgeList):
        count = 0
        for i in edgeList:
            print(i)
            count +=1
        return count

    def clearList(self,list):
        del list[:]
        return list



    def get_list(self,b,s,currentPath,path_list,count):
        cPath = currentPath.copy()


        if(count == 0):
            return path_list


        for i in b.edges:

            if(b == i.u):

                new = self.opposite(i,b)
            else:
                new = i.u

            if(new not in currentPath):


                # print("amount of edge of new " + str(len(new.edges)))
                if(new == s):
            #         ## found destination. add to return path list
                    # print(new);
                    count -=1;
                    cPath.append(new)
                    path_list.append(cPath)
                    del currentPath[1:]




                elif ((len(new.edges)==1) and (new.edges[0].v == new or new.edges[0].u == new)):
                    # print("This is new: " + str(new))
                    del currentPath[1:]

                else:
                    currentPath.append(new)
                    # print(new)

                    path_list =  self.get_list(new, s, currentPath,path_list,count)
        return path_list



    def MinCalculateDistance(self,list):
        i = 0
        largest = 0
        total = []
        while (i+1)< len(list):
            total.append(self.distance(list[0],list[i+1]))
            i+=1


        for num in total:
            if(num>largest):
                largest = num

        return largest


    def inRange(self,r,list):
        status = True
        i = 0
        distance = 0
        while i+1 < len(list):
            distance = self.distance(list[0],list[i+1])
            if(distance>r):
                status = False
            i+=1
        return status






    def find_path(self, b, s, r):


        """
        Find a path from vertex B to vertex S, such that the distance from B to
        every vertex in the path is within R.  If there is no path between B
        and S within R, then return None.

        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :param r: The maximum range of the radio.
        :return: The LIST of the VERTICES in the path.
        """
        if(b == s):


            return [b]
        if (r == 0):
            return None

        if(len(b.edges) ==1 and (b.edges[0].v == b)):
            return None

        path_list = []
        currentPath = [b]
        print(b,s);
        count = len(b.edges)
        path_list = self.get_list(b,s,currentPath,path_list,count)


        status = False
        i = 0
        for j in path_list:
            status = self.inRange(r,j)
            if(status == True):
                return j


        return None






    def minimum_range(self, b, s):
        """
        Returns the minimum range required to go from Vertex B to Vertex S.
        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :return: The minimum range in the path to go from B to S.
        """
        # TODO implement me!
        if(b == s):
            return 0
        #If there is only Two
        path_list = []
        currentPath = [b]
        count = len(s.edges)
        path_list = self.get_list(b,s,currentPath,path_list,count)

        # print(path_list)
        # print(b.edges[0],s.edges[0])
        # return None;

        largest = []
        smallest = 1000000
        for i in path_list:
            largest_distance = self.MinCalculateDistance(i)
            largest.append(largest_distance)
        for m in largest:

            if(m<smallest):
                smallest = m




        return round(smallest,5)
        # return 0

    def move_vertex(self, v, new_x, new_y):
        """
        Move the defined vertex.

        If there is already a vertex there, do nothing.

        :param v: The vertex to move
        :param new_x: The new X position
        :param new_y: The new Y position
        """
        status = False

        for i in self._vertices:
            if(i.x_pos == new_x and i.y_pos == new_y):
                status = True
        if(status == False):
            v.x_pos = new_x
            v.y_pos = new_y
#

# G = Graph()
#
# # Layer 1
# A = G.insert_vertex(0, 0)
#
# # Layer 2
# B = G.insert_vertex(2, 0)
# C = G.insert_vertex(2, 98)
# D = G.insert_vertex(2, 99)
#
# # Layer 3
# E = G.insert_vertex(3, 3)
# F = G.insert_vertex(4, 6)
#
# # Make the edges
# G.insert_edge(A, B)
# G.insert_edge(A, C)
# G.insert_edge(A, D)
# G.insert_edge(C, E)
# G.insert_edge(C, F)
# G.insert_edge(D, F)
#
# # Find the minimum range
#
# r = G.minimum_range(A, F)
# print(r)
# # expected_r = 98.02041
