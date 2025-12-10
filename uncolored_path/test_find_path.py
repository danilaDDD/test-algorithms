import numpy as np

from uncolored_path.find_path import find_first_full_path


class TestFindPath:
    def test_with_one_node_graph(self):
        paths = find_first_full_path(np.array([[1]]))
        assert paths == [[0]]

    def test_with_linear_graph(self):
        paths = find_first_full_path(np.array([
            [0, 1],
            [1, 0]
        ]))

        assert paths == [[0, 1], [1, 0]]

    def test_with_triangle_graph(self):
        paths = find_first_full_path(np.array([
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]))

        assert paths == [
            [0, 1, 2],
            [1, 0, 2],
            [1, 2, 0],
        ]


