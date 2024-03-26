import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("abab", "bold")
        node2 = TextNode("cdcd","bold")
        self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("a","italics")
        node2 = TextNode("a", "bold")
        self.assertNotEqual(node, node2)

    def test_neq3(self):
        node = TextNode("a","bold","http://localhost")
        node2 = TextNode("a","bold","http://www.google.com")
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = TextNode("a","bold","http://localhost")
        node2 = TextNode("a","bold","http://localhost")
        self.assertEqual(node, node2)

    def test_ne4(self):
        node = TextNode("a","bold")
        node2 = TextNode("a","bold","http://localhost")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
