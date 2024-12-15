from collections import deque

class Dinic:
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.adj = [[] for _ in range(vertices)]  # Список смежности
        self.capacity = {}  # Словарь для хранения пропускных способностей

    def add_edge(self, u, v, cap):
        """Добавляет ребро в сеть с заданной пропускной способностью."""
        self.adj[u].append(v)
        self.adj[v].append(u)  # Добавляем обратное ребро
        self.capacity[(u, v)] = cap  # Пропускная способность прямого ребра
        self.capacity[(v, u)] = 0  # Пропускная способность обратного ребра

    def bfs(self, source, sink):
        """Поиск в ширину для построения уровня графа."""
        self.level = [-1] * self.V
        queue = deque([source])
        self.level[source] = 0

        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if self.level[v] < 0 and self.capacity[(u, v)] > 0:  # Если не посещен и есть остаточная пропускная способность
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
                    if v == sink:
                        return True
        return False

    def dfs(self, u, sink, flow):
        """Поиск в глубину для нахождения блокирующего потока."""
        if u == sink:
            return flow
        for v in self.adj[u]:
            if self.level[v] == self.level[u] + 1 and self.capacity[(u, v)] > 0:  # Если уровень следующий и есть остаточная пропускная способность
                current_flow = min(flow, self.capacity[(u, v)])
                temp_flow = self.dfs(v, sink, current_flow)
                if temp_flow > 0:  # Если поток был найден
                    # Уменьшаем пропускную способность прямого ребра и увеличиваем обратного
                    self.capacity[(u, v)] -= temp_flow
                    self.capacity[(v, u)] += temp_flow
                    return temp_flow
        return 0

    def max_flow(self, source, sink):
        """Основной метод для нахождения максимального потока."""
        total_flow = 0
        
        while True:
            if not self.bfs(source, sink):  # Построение уровня графа
                break
            
            while True:
                flow = self.dfs(source, sink, float('Inf'))  # Находим блокирующий поток
                if flow == 0:
                    break
                total_flow += flow
        
        return total_flow

# Пример использования
if __name__ == "__main__":
    g = Dinic(6)  # Создаем граф с 6 вершинами (0-5)

    g.add_edge(0, 1, 16)
    g.add_edge(0, 2, 13)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 12)
    g.add_edge(2, 1, 4)
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9)
    g.add_edge(3, 5, 20)
    g.add_edge(4, 3, 7)
    g.add_edge(4, 5, 4)

    source = 0   # Исходная вершина
    sink = 5     # Конечная вершина

    print("Максимальный поток:", g.max_flow(source, sink))
