"""
list of acceptable textnode types:
text
bold
italic
code
link
image
"""

from htmlnode import HTMLNode, LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, node) -> bool:
        return self.text == node.text and self.text_type == node.text_type and self.url == node.url
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node) -> HTMLNode:
    type = text_node.text_type
    if type == "text":
        return LeafNode(value=text_node.text)
    if type == "bold":
        return LeafNode(tag='b',value=text_node.text)
    if type == "italic":
        return LeafNode(tag='i',value=text_node.text)
    if type == "code":
        return LeafNode(tag='code',value=text_node.text)
    if type == "link":
        return LeafNode(tag='a',value=text_node.text,props={"href":text_node.url})
    if type == "image":
        return LeafNode(tag="img",value="",props={"src":text_node.url,"alt":text_node.text})
    raise ValueError(f"Invalid text_type of TextNode object: {text_node.text_type}")