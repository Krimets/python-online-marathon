class LeafElement:
    def __init__(self, *args):
        self.position = args[0]

    def showDetails(self):
        print("\t", end="")
        print(self.position)


class CompositeElement:
    def __init__(self, *args):
        self.position = args[0]
        self.kids = []

    def add(self, child):
        self.kids.append(child)

    def remove(self, child):
        self.kids.remove(child)

    def showDetails(self):
        print(self.position)
        for child in self.kids:
            print("\t", end="")
            child.showDetails()
