import unittest
import components.UnweightedEdge as edge
import components.Vertex as vertex
import graphasedgelist.GraphAsEdgeList as graph


class MyTestCase(unittest.TestCase):
    def test_something(self):
        el_graph = graph.GraphAsEdgeList()
        # social media people
        rama = vertex.Vertex("rama")
        ella = vertex.Vertex("ella")
        bob = vertex.Vertex("bob")
        tom = vertex.Vertex("tom")
        lee = vertex.Vertex("lee")
        sam = vertex.Vertex("sam")
        katie = vertex.Vertex("katie")
        zahir = vertex.Vertex("zahir")
        swati = vertex.Vertex("swati")
        arun = vertex.Vertex("arun")

        el_graph.add_vertex(rama)
        el_graph.add_vertex(ella)
        el_graph.add_vertex(bob)
        el_graph.add_vertex(tom)
        el_graph.add_vertex(lee)
        el_graph.add_vertex(sam)
        el_graph.add_vertex(katie)
        el_graph.add_vertex(zahir)
        el_graph.add_vertex(swati)
        el_graph.add_vertex(arun)

        # rama has three friends
        rta = edge.UnweightedEdge(rama, ella)
        rtb = edge.UnweightedEdge(rama, bob)
        rtk = edge.UnweightedEdge(rama, katie)
        el_graph.add_edge(rta)
        el_graph.add_edge(rtb)
        el_graph.add_edge(rtk)

        # ella has two friends
        etr = edge.UnweightedEdge(ella, rama)
        etb = edge.UnweightedEdge(ella, bob)
        el_graph.add_edge(etr)
        el_graph.add_edge(etb)

        # bob has 5 friends
        bte = edge.UnweightedEdge(bob, ella)
        btr = edge.UnweightedEdge(bob, rama)
        btl = edge.UnweightedEdge(bob, lee)
        bts = edge.UnweightedEdge(bob, sam)
        btt = edge.UnweightedEdge(bob, tom)
        el_graph.add_edge(bte)
        el_graph.add_edge(btr)
        el_graph.add_edge(btl)
        el_graph.add_edge(bts)
        el_graph.add_edge(btt)

        # tom has two friends
        ttb = edge.UnweightedEdge(tom, bob)
        tts = edge.UnweightedEdge(tom, sam)
        el_graph.add_edge(ttb)
        el_graph.add_edge(tts)

        # lee has 5 friends
        ltb = edge.UnweightedEdge(lee, bob)
        lts = edge.UnweightedEdge(lee, sam)
        ltz = edge.UnweightedEdge(lee, zahir)
        lts = edge.UnweightedEdge(lee, swati)
        ltk = edge.UnweightedEdge(lee, katie)
        el_graph.add_edge(ltb)
        el_graph.add_edge(lts)
        el_graph.add_edge(ltz)
        el_graph.add_edge(lts)
        el_graph.add_edge(ltk)

        # sam has 5 friends
        stt = edge.UnweightedEdge(sam, tom)
        stb = edge.UnweightedEdge(sam, bob)
        stl = edge.UnweightedEdge(sam, lee)
        stz = edge.UnweightedEdge(sam, zahir)
        sta = edge.UnweightedEdge(sam, arun)
        el_graph.add_edge(stt)
        el_graph.add_edge(stb)
        el_graph.add_edge(stl)
        el_graph.add_edge(stz)
        el_graph.add_edge(sta)

        # katie has 3 friends
        ktr = edge.UnweightedEdge(katie, rama)
        ktl = edge.UnweightedEdge(katie, lee)
        kts = edge.UnweightedEdge(katie, swati)
        el_graph.add_edge(ktr)
        el_graph.add_edge(ktl)
        el_graph.add_edge(kts)

        # zahir has 4 friends
        zts = edge.UnweightedEdge(zahir, sam)
        zta = edge.UnweightedEdge(zahir, arun)
        ztz = edge.UnweightedEdge(zahir, swati)
        ztl = edge.UnweightedEdge(zahir, lee)
        el_graph.add_edge(zts)
        el_graph.add_edge(zta)
        el_graph.add_edge(ztz)
        el_graph.add_edge(ztl)

        # swati has 3 friends
        stk = edge.UnweightedEdge(swati, katie)
        sts = edge.UnweightedEdge(swati, lee)
        st2 = edge.UnweightedEdge(swati, zahir)
        el_graph.add_edge(stk)
        el_graph.add_edge(sts)
        el_graph.add_edge(st2)

        # arun has 2 friends
        atz = edge.UnweightedEdge(arun, zahir)
        ats = edge.UnweightedEdge(arun, sam)
        el_graph.add_edge(atz)
        el_graph.add_edge(ats)

        print(el_graph.are_vertices_connected(rama, ella))
        print(el_graph.are_vertices_connected(rama, tom))

        adjancent_vertices = el_graph.get_adjancent_vertices(rama)
        for items in adjancent_vertices:
            print(items.value + " is friends with " + rama.value)

        adjancent_vertices = el_graph.get_adjancent_vertices(sam)
        for items in adjancent_vertices:
            print(items.value + " is friends with " + sam.value)

        el_graph.print_all_edges()
        el_graph.print_all_vertices()


if __name__ == '__main__':
    unittest.main()
