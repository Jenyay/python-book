import unittest
from triangle import Triangle

class TriangleTests(unittest.TestCase):
    def testInit(self):
        p1 = (0.0, 0.0)
        p2 = (0.0, 1.0)
        p3 = (2.0, 0.0)
        triangle = Triangle(p1, p2, p3)
        self.assertEqual(triangle[0], p1)
        self.assertEqual(triangle[1], p2)
        self.assertEqual(triangle[2], p3)

if __name__ == "__main__":
    unittest.main()
