import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(props={"href":"https://www.google.com", "target": "_blank"})
        target = " href=\"https://www.google.com\" target=\"_blank\""
        #print("expecting: " + target)
        #print("actual: "+node1.props_to_html())
        self.assertEqual(node1.props_to_html(),target)

    def test2_props_to_html(self):
        node1 = HTMLNode()
        target = ""
        #print("expecting: "+target)
        #print("actual: "+node1.props_to_html())
        self.assertEqual(node1.props_to_html(),target)

    def test_repr(self):
        node1 = HTMLNode(tag="p",value="hello world")
        node4 = HTMLNode(value="blah")
        node2 = HTMLNode(tag="a",value="link_here",children=[node1,node4])
        node3 = HTMLNode(children=[node2])
        print(node1)
        print(node2)
        print(node3)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
