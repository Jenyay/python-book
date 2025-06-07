import unittest
from triangle import Triangle

class TriangleTests(unittest.TestCase):
    def testInit(self):
        p1 = (0.0, 0.0)
        p2 = (0.0, 1.0)
        p3 = (2.0, 0.0)
        triangle = Triangle(p1, p2, p3)
        self.assertEqual(triangle[0], p1, "Координата первой вершины")
        self.assertEqual(triangle[1], p2, "Координата второй вершины")
        self.assertEqual(triangle[2], p3, "Координата третьей вершины")

    def testSides(self):
        p1 = (0.0, 0.0)
        p2 = (0.0, 1.0)
        p3 = (2.0, 0.0)
        triangle = Triangle(p1, p2, p3)
        self.assertAlmostEqual(triangle.side_len(0, 1), 1, delta=1e-5)
        self.assertAlmostEqual(triangle.side_len(0, 2), 2, delta=1e-5)
        self.assertAlmostEqual(triangle.side_len(1, 2), 2.236, places=3)

if __name__ == "__main__":
    unittest.main()
