import unittest
import components.UnweightedEdge as edge
import components.Vertex as vertex
import graphasedgelist.GraphAsEdgeList as graph


class MyTestCase(unittest.TestCase):
    def test_something(self):
        el_graph = graph()
        # social media people
        rama = vertex("rama")
        ella = vertex("ella")
        bob = vertex("bob")
        tom = vertex("tom")
        lee = vertex("lee")
        sam = vertex("sam")
        katie = vertex("katie")
        zahir = vertex("zahir")
        swati = vertex("swati")
        arun = vertex("arun")

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
        rta = edge(rama, ella)
        rtb = edge(rama, bob)
        rtk = edge(rama, katie)
        el_graph.add_edge(rta)
        el_graph.add_edge(rtb)
        el_graph.add_edge(rtk)

        # ella has two friends
        etr = edge(ella, rama)
        etb = edge(ella, bob)
        el_graph.add_edge(etr)
        el_graph.add_edge(etb)

        # bob has 5 friends
        bte = edge(bob, ella)
        btr = edge(bob, rama)
        btl = edge(bob, lee)
        bts = edge(bob, sam)
        btt = edge(bob, tom)
        el_graph.add_edge(bte)
        el_graph.add_edge(btr)
        el_graph.add_edge(btl)
        el_graph.add_edge(bts)
        el_graph.add_edge(btt)

        # tom has two friends
        ttb = edge(tom, bob)
        tts = edge(tom, sam)
        el_graph.add_edge(ttb)
        el_graph.add_edge(tts)

        # lee has 5 friends
        ltb = edge(lee, bob)
        lts = edge(lee, sam)
        ltz = edge(lee, zahir)
        lts = edge(lee, swati)
        ltk = edge(lee, katie)
        el_graph.add_edge(ltb)
        el_graph.add_edge(lts)
        el_graph.add_edge(ltz)
        el_graph.add_edge(lts)
        el_graph.add_edge(ltk)

        # sam has 5 friends
        stt = edge(sam, tom)
        stb = edge(sam, bob)
        stl = edge(sam, lee)
        stz = edge(sam, zahir)
        sta = edge(sam, arun)
        el_graph.add_edge(stt)
        el_graph.add_edge(stb)
        el_graph.add_edge(stl)
        el_graph.add_edge(stz)
        el_graph.add_edge(sta)

        # katie has 3 friends
        ktr = edge(katie, rama)
        ktl = edge(katie, lee)
        kts = edge(katie, swati)
        el_graph.add_edge(ktr)
        el_graph.add_edge(ktl)
        el_graph.add_edge(kts)

        # zahir has 4 friends
        zts = edge(zahir, sam)
        zta = edge(zahir, arun)
        ztz = edge(zahir, swati)
        ztl = edge(zahir, lee)
        el_graph.add_edge(zts)
        el_graph.add_edge(zta)
        el_graph.add_edge(ztz)
        el_graph.add_edge(ztl)

        # swati has 3 friends
        stk = edge(swati, katie)
        sts = edge(swati, lee)
        st2 = edge(swati, zahir)
        el_graph.add_edge(stk)
        el_graph.add_edge(sts)
        el_graph.add_edge(st2)

        # arun has 2 friends
        atz = edge(arun, zahir)
        ats = edge(arun, sam)
        el_graph.add_edge(atz)
        el_graph.add_edge(ats)


if __name__ == '__main__':
    unittest.main()
