import unittest

from mathx import clamp


class TestClamp(unittest.TestCase):
    def test_inside_range_unchanged(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_below_lo_returns_lo(self):
        self.assertEqual(clamp(-3, 0, 10), 0)

    def test_above_hi_returns_hi(self):
        self.assertEqual(clamp(42, 0, 10), 10)

    def test_boundaries_inclusive(self):
        self.assertEqual(clamp(0, 0, 10), 0)
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_lo_equals_hi(self):
        self.assertEqual(clamp(7, 3, 3), 3)

    def test_floats(self):
        self.assertEqual(clamp(1.5, 0.0, 1.0), 1.0)

    def test_lo_greater_than_hi_raises(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)
        with self.assertRaises(ValueError):
            clamp(10, 10, 0)


if __name__ == "__main__":
    unittest.main()
