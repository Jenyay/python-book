import unittest
from triangle import Triangle

class TriangleTests(unittest.TestCase):
    def setUp(self):
        self.p1 = (0.0, 0.0)
        self.p2 = (0.0, 1.0)
        self.p3 = (2.0, 0.0)
        self.triangle = Triangle(self.p1, self.p2, self.p3)

    def testInit(self):
        self.assertEqual(self.triangle[0], self.p1,
                         "Координата первой вершины")
        self.assertEqual(self.triangle[1], self.p2,
                         "Координата второй вершины")
        self.assertEqual(self.triangle[2], self.p3,
                         "Координата третьей вершины")

    def testSides(self):
        self.assertAlmostEqual(self.triangle.side_len(0, 1), 1,
                               delta=1e-5)
        self.assertAlmostEqual(self.triangle.side_len(0, 2), 2,
                               delta=1e-5)
        self.assertAlmostEqual(self.triangle.side_len(1, 2), 2.236,
                               places=3)

    def testSidesIndexError1(self):
        self.assertRaises(ValueError, self.triangle.side_len, -1, 0)

    def testSidesIndexError2(self):
        with self.assertRaises(ValueError):
            self.triangle.side_len(2, 3)

if __name__ == "__main__":
    unittest.main()
