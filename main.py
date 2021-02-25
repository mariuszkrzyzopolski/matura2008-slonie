class Graph:
    def __init__(self):
        with open("slo1.in") as f:
            self.content = f.readlines()
            self.group = []

    def cycles(self, result, point):
        if point in result.keys():
            proceed = result[point]
            self.group.append(point)
            result.pop(point)
            self.cycles(result, proceed)
            return self.group

    def edges(self):
        result = dict()
        slin = self.content[2].split(" ")
        slout = self.content[3].split(" ")
        for index, el in enumerate(slin):
            result.update({int(el): int(slout[index])})
        return self.cycles(result, 1)


if __name__ == '__main__':
    graph = Graph()
    print(graph.edges())
