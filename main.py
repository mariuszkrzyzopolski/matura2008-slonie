import sys


class Graph:
    result = {}

    def __init__(self):
        self.content = sys.stdin.readlines()
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
        return list(filter(None, g))

    def method1(self, wages):
        return sum(wages) + (len(wages) - 2) * min(wages)

    def method2(self, wages, global_minimal):
        return sum(wages) + min(wages) + (len(wages) + 1) * global_minimal

    def order(self, group):
        wages = []
        origin_wages = self.content[1].split(" ")
        for el in group:
            wages.append(int(origin_wages[el - 1]))
        res1 = self.method1(wages)
        res2 = self.method2(wages, min(map(int, origin_wages)))
        if res1 < res2:
            return res1
        else:
            return res2


if __name__ == '__main__':
    graph = Graph()
    # print(graph.edges())
    sumOfAllGroups = 0
    for cycle in graph.edges():
        if len(cycle) > 1:
            sumOfAllGroups += graph.order(cycle)
    print(sumOfAllGroups)
