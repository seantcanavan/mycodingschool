import dynamiclistasarray.DynamicListAsArray as arraylist


# space complexity = O ( |e| + |v| )

class GraphAsEdgeList:
    vertex_list = arraylist.DynamicListAsArray()
    edge_list = arraylist.DynamicListAsArray()

    def add_vertex(self, input_vertex):
        self.vertex_list.add(input_vertex)

    def add_edge(self, input_edge):
        self.edge_list.add(input_edge)

    # O( |e| )
    def get_adjancent_vertices(self, vertex):
        adjacent_vertices = []
        for x in range(0, self.edge_list.get_size()):
            current_edge = self.edge_list.get_at(x)
            if current_edge.start.value == vertex.value:
                adjacent_vertices.append(current_edge.end)
        return adjacent_vertices

    # O( |v| )
    def are_vertices_connected(self, vertex1, vertex2):
        for x in range(0, self.edge_list.get_size()):
            current_edge = self.edge_list.get_at(x)
            if vertex1.value == current_edge.start.value and vertex2.value == current_edge.end.value:
                return True
        return False

    # O( |e| )
    def print_all_edges(self):
        for x in range(0, self.edge_list.get_size()):
            current = self.edge_list.get_at(x)
            print("start: " + current.start.value + " end: " + current.end.value)

    # O( |v| )
    def print_all_vertices(self):
        for x in range(0, self.vertex_list.get_size()):
            current = self.vertex_list.get_at(x)
            print("vertex: " + current.value)