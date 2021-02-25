class Graph:
    result = {}

    def __init__(self):
        with open("slo1.in") as f:
            self.content = f.readlines()
        self.group = []

    def cycles(self, point):
        if point in self.result.keys():
            proceed = self.result[point]
            self.group.append(point)
            self.result.pop(point)
            self.cycles(proceed)
            return self.group

    def edges(self):
        result = dict()
        slin = self.content[2].split(" ")
        slout = self.content[3].split(" ")
        for index, el in enumerate(slin):
            self.result.update({int(el): int(slout[index])})
        g = []
        i = 1
        while self.result:
            g.append(self.cycles(i))
            self.group = []
            i += 1
            #need reverse every list
        return list(filter(None, g))


if __name__ == '__main__':
    graph = Graph()
    print(graph.edges())
    print(graph.result)
