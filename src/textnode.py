from enum import Enum

from leafnode import LeafNode

def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(tag="", value=text_node.raw)
        elif text_node.text_type == TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        elif text_node.text_type == TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        elif text_node.text_type == TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        else:
            raise ValueError(f"Unknown text type: {text_node.text_type}")

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type =text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode(text={self.text}, text_type={self.text_type}, url={self.url})"