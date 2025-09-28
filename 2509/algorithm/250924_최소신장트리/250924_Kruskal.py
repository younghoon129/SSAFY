class DisjointSet:

    def __init__(self, v):  # 정점들만큼 p_list, rank 만듦
        self.p = [0] * (len(v) + 1)
        self.rank = [0] * (len(v) + 1)

    def make_set(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px
            else:
                self.p[py] = px
                self.rank[px] += 1

def mst_kruskal(vertices, edges):
    mst = []

    ds = DisjointSet(vertices)  # 바로 init 실행해서 넣음
    for i in range(len(vertices) + 1):  # self.p가 vertices에 0 추가 되니까 +1
        ds.make_set(i)  # 각 정점들에 부모 부여

    edges.sort(key=lambda x: x[2])

    for edge in edges:  # 가중치 기준 정렬된 edges
        s, e, w = edge  # s = 시작, e = 도착, w = 가중치
        if ds.find_set(s) != ds.find_set(e):  # s의 부모가 e의 부모랑 다르면(사이클 안하기위해)
            ds.union_set(s, e)  # 합침
            mst.append(edge)  # 결과에 간선 넣음
    return mst  # 부모 같으면 안넣고 리턴


edges = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]
vertices = [1, 2, 3]

# vertices = 정점들, edges = 간선들
result = mst_kruskal(vertices, edges)

print(result)

edges = [
    (0, 1, 32),
    (0, 2, 31),
    (0, 5, 60),
    (0, 6, 51),
    (1, 2, 21),
    (2, 4, 46),
    (2, 6, 25),
    (3, 4, 34),
    (3, 5, 18),
    (4, 5, 40),
    (4, 6, 51),
]
vertices = list(range(7))

result = mst_kruskal(vertices, edges) 
print(result)

