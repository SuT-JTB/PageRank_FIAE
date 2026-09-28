class Page:
    def __init__(self, id: str, rank: float, outLink: list, inLink: list):
        self.id = id
        self.rank = rank
        self.outLink = outLink
        self.inLink = inLink

    def inOutLink(self, page: Page) -> None:
        self.outLink.append(page)
        page.inLink.append(self)


class Graph:
    def __init__(self, page: list[Page]):
        self.pages = page

    def addPage(self, page: Page) -> None:
        self.pages.append(page)

    def calculate(self, d: float, iterations: int) -> None:
        if iterations < 1:
            raise ValueError("iterations must not be negative")
        if not 0 <= d <= 1:
            raise ValueError("damping factor outside valid range.(0.0~1.0)")

        for _ in range(iterations):
            for page in self.pages:
                page.rank = (1 - d) + d * sum(
                    inPage.rank / len(inPage.outLink) for inPage in page.inLink
                )

    def printRanks(self):
        for page in self.pages:
            print(f"{page.id}: {str(round(page.rank, 3))}")


def scenario_1():

    A1 = Page("A1", 1, [], [])
    B1 = Page("B1", 1, [], [])
    C1 = Page("C1", 1, [], [])
    D1 = Page("D1", 1, [], [])

    A1.inOutLink(B1)
    A1.inOutLink(C1)
    B1.inOutLink(C1)
    C1.inOutLink(A1)
    D1.inOutLink(B1)
    D1.inOutLink(A1)
    D1.inOutLink(C1)

    Graph1 = Graph([A1, B1, C1, D1])
    Graph1.calculate(0.85, 20)
    Graph1.printRanks()


def scenario_2():
    import random

    A1 = Page("A1", 1, [], [])
    B1 = Page("B1", 1, [], [])
    C1 = Page("C1", 1, [], [])
    D1 = Page("D1", 1, [], [])
    E1 = Page("E1", 1, [], [])
    F1 = Page("F1", 1, [], [])
    G1 = Page("G1", 1, [], [])
    H1 = Page("H1", 1, [], [])
    I1 = Page("I1", 1, [], [])
    J1 = Page("J1", 1, [], [])
    K1 = Page("K1", 1, [], [])

    pages = [A1, B1, C1, D1, E1, F1, G1, H1, I1, J1, K1]
    [
        page.inOutLink(link)
        for page in pages
        for link in random.sample(
            [p for p in pages if p is not page], random.randint(1, len(pages) - 1)
        )
    ]

    Graph1 = Graph(pages)
    Graph1.calculate(0.85, 20)
    Graph1.printRanks()


def scenario_excel():

    A1 = Page("A1", 1, [], [])
    B1 = Page("B1", 1, [], [])
    C1 = Page("C1", 1, [], [])

    A1.inOutLink(B1)
    A1.inOutLink(C1)
    B1.inOutLink(C1)
    C1.inOutLink(A1)

    Graph1 = Graph([A1, B1, C1])
    Graph1.calculate(0.85, 20)
    Graph1.printRanks()


if __name__ == "__main__":
    # scenario_1()
    # scenario_2()
    scenario_excel()
