import unittest

from pageRankCalculator import Graph, Page


class TestPageRank(unittest.TestCase):
    def test_addPage_appends_new_page(self):
        graph = Graph([])
        page = Page("A", 1.0, [], [])

        graph.addPage(page)

        self.assertIn(page, graph.pages)

    def test_inOutLink_creates_bidirectional_link(self):
        a = Page("A", 1.0, [], [])
        b = Page("B", 1.0, [], [])

        a.inOutLink(b)

        self.assertIn(b, a.outLink)
        self.assertIn(a, b.inLink)

    def test_graph_calculate_raises_on_negative_iterations(self):
        graph = Graph([Page("A", 1.0, [], [])])

        with self.assertRaises(ValueError):
            graph.calculate(0.85, 0)

    def test_graph_calculate_raises_on_invalid_damping(self):
        graph = Graph([Page("A", 1.0, [], [])])

        with self.assertRaises(ValueError):
            graph.calculate(1.5, 5)

    def test_graph_calculate_updates_rank_for_known_graph(self):
        a = Page("A", 1.0, [], [])
        b = Page("B", 1.0, [], [])
        c = Page("C", 1.0, [], [])

        a.inOutLink(b)
        a.inOutLink(c)
        b.inOutLink(c)
        c.inOutLink(a)

        graph = Graph([a, b, c])
        graph.calculate(0.85, 1)

        self.assertAlmostEqual(a.rank, 1.0, places=6)
        self.assertAlmostEqual(b.rank, 0.575, places=6)
        self.assertAlmostEqual(c.rank, 1.06375, places=6)


if __name__ == "__main__":
    unittest.main()