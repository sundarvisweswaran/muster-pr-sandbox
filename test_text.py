import unittest
from text import slug


class SlugTest(unittest.TestCase):
    def test_slug(self):
        self.assertEqual(slug("Hello World"), "hello-world")


if __name__ == "__main__":
    unittest.main()
