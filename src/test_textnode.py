import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
        
    def test_neq(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)
        
    def test_neq2(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        node2 = TextNode("This is a text node!", TextType.NORMAL_TEXT)
        self.assertNotEqual(node, node2)
        
    def test_eq_url(self):
        node = TextNode("This is a node", TextType.LINK, "http://www.google.com")
        node2 = TextNode("This is a node", TextType.LINK, "http://www.google.com")
        self.assertEqual(node, node2)  


if __name__ == "__main__":
    unittest.main()