import dynamiclistasarray.DynamicListAsArray as arraylist


# space complexity = O ( |e| + |v| )

class GraphAsEdgeList:
    vertex_list = arraylist()
    edge_list = arraylist()

    def add_vertex(self, input_vertex):
        self.vertex_list.append(input_vertex)

    def add_edge(self, input_edge):
        self.edge_list.append(input_edge)

    #O ( |e| )
    def find_all_adjactent_nodes(self):
        print("hi")


    def are_vertexes_connected(self, vertex1, vertex2):
        print("hi")


