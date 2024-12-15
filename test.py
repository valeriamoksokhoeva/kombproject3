import unittest

class TestDinicAlgorithm(unittest.TestCase):
    def setUp(self):
        """Создаем экземпляр графа для тестирования."""
        self.graph = Dinic(6)
        self.graph.add_edge(0, 1, 16)
        self.graph.add_edge(0, 2, 13)
        self.graph.add_edge(1, 2, 10)
        self.graph.add_edge(1, 3, 12)
        self.graph.add_edge(2, 1, 4)
        self.graph.add_edge(2, 4, 14)
        self.graph.add_edge(3, 2, 9)
        self.graph.add_edge(3, 5, 20)
        self.graph.add_edge(4, 3, 7)
        self.graph.add_edge(4, 5, 4)

    def test_max_flow(self):
        """Тестируем максимальный поток в графе."""
        source = 0
        sink = 5
        expected_flow = 23
        actual_flow = self.graph.max_flow(source, sink)
        self.assertEqual(actual_flow, expected_flow)

    def test_no_flow(self):
        """Тестируем случай с отсутствием потока."""
        empty_graph = Dinic(2)  # Граф с двумя вершинами и без рёбер
        source = 0
        sink = 1
        expected_flow = 0
        actual_flow = empty_graph.max_flow(source, sink)
        self.assertEqual(actual_flow, expected_flow)

    def test_single_path(self):
        """Тестируем граф с единственным путем от источника к стоку."""
        single_path_graph = Dinic(3) 
        single_path_graph.add_edge(0, 1, 10)
        single_path_graph.add_edge(1, 2, 5)

        source = 0
        sink = 2
        expected_flow = 5
        actual_flow = single_path_graph.max_flow(source, sink)
        self.assertEqual(actual_flow, expected_flow)

    def test_multiple_paths(self):
        """Тестируем граф с несколькими путями."""
        multi_path_graph = Dinic(5) 
        multi_path_graph.add_edge(0, 1, 10)
        multi_path_graph.add_edge(0, 2, 10)
        multi_path_graph.add_edge(1, 3, 5)
        multi_path_graph.add_edge(2, 3, 15)
        multi_path_graph.add_edge(3, 4, 10)

        source = 0
        sink = 4
        expected_flow = 15
        actual_flow = multi_path_graph.max_flow(source, sink)
        self.assertEqual(actual_flow, expected_flow)

if __name__ == "__main__":
    unittest.main()
