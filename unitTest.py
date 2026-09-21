import unittest

class Page:
    def __init__(self, id: str, rank: float, outLink: list, inLink: list):
        self.id = id
        self.rank = rank
        self.outLink = outLink
        self.inLink = inLink

    def inOutLink(self, page: "Page") -> None:
        self.outLink.append(page)
        page.inLink.append(self)

class Graph:
    def __init__(self, pages: list[Page]):
        self.pages = pages

    def calculate(self, d: float, iterations: int) -> None:
        if iterations < 1:
            raise ValueError("iterations must not be negative")
        if not 0 <= d <= 1:
            raise ValueError("damping factor outside valid range.(0.0~1.0)")

        for _ in range(iterations):
            for page in self.pages:
                page.rank = (1 - d) + d * sum(
                    inPage.rank / len(inPage.outLink)
                    for inPage in page.inLink
                )

class TestPageRank(unittest.TestCase):
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

    def test_graph_calculate_updates_rank(self):
        a = Page("A", 1.0, [], [])
        b = Page("B", 1.0, [], [])

        a.inOutLink(b)

        graph = Graph([a, b])
        graph.calculate(0.85, 1)

        self.assertGreater(a.rank, 0)
        self.assertGreater(b.rank, 0)

if __name__ == "__main__":
    unittest.main()