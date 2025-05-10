class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.tag = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Convert the HTMLNode to an HTML string.
        """
        raise NotImplementedError("Subclasses should implement this method.")
    
    def props_to_html(self):
        """
        Convert the properties of the HTMLNode to an HTML string.
        """
        if not self.props:
            return ""
        
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        
        return result
    
    def __repr__(self):
        """
        Return a string representation of the HTMLNode.
        """
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"