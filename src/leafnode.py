from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, attributes=None):
        # For a leaf node, children should always be an empty list
        super().__init__(tag, [], value, attributes)
        
    def to_html(self):
        # First check if value exists
        if self.value is None:
            raise ValueError("LeafNode must have a value")
    
        # If no tag, return the raw value
        if self.tag is None:
            return self.value       

        # Start building the opening tag
        html = f"<{self.tag}"
        
        # Add attributes if they exist
        if self.attributes:
            for attr, val in self.attributes.items():
                html += f' {attr}="{val}"'
        
        # Close the opening tag and add the value and closing tag
        html += f">{self.value}</{self.tag}>"
        
        return html