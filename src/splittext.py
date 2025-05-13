from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        new_nodes.append(node)

        if node.text_type == TextType.TEXT:
            split = node.text.split(delimiter)

            for i, piece in enumerate(split):
                if i % 2 == 0:
                    new_nodes.append(TextNode(piece, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(piece, text_type))
    return new_nodes