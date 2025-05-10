import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_equal(self):
        return self.assertEqual(
            TextNode("This is a text node", TextType.BOLD),
            TextNode("This is a text node", TextType.BOLD)
        )
    def test_not_equal(self):
        return self.assertNotEqual(
            TextNode("This is a text node", TextType.BOLD),
            TextNode("This is a text node", TextType.ITALIC)
        )



if __name__ == "__main__":
    unittest.main()