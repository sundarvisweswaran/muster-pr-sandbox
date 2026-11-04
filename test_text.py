import unittest
from text import slug, snake_case, title_case


class SlugTest(unittest.TestCase):
    def test_slug(self):
        self.assertEqual(slug("Hello World"), "hello-world")

    def test_title_case(self):
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("hello  world"), "Hello  World")

    def test_snake_case(self):
        self.assertEqual(snake_case("Hello World"), "hello_world")
        self.assertEqual(snake_case("  Hello   World "), "hello_world")


if __name__ == "__main__":
    unittest.main()
