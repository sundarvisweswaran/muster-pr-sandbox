import unittest
from text import slug, title_case


class SlugTest(unittest.TestCase):
    def test_slug(self):
        self.assertEqual(slug("Hello World"), "hello-world")

    def test_title_case(self):
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("hello  world"), "Hello  World")


if __name__ == "__main__":
    unittest.main()
