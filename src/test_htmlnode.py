from htmlnode import HTMLNode

def test_props_to_html_empty():
    # Test with no props
    node = HTMLNode(props=None)
    assert node.props_to_html() == ""
    
    # Test with empty props dict
    node = HTMLNode(props={})
    assert node.props_to_html() == ""

def test_props_to_html_single_prop():
    # Test with a single prop
    node = HTMLNode(props={"href": "https://www.google.com"})
    assert node.props_to_html() == ' href="https://www.google.com"'

def test_props_to_html_multiple_props():
    # Test with multiple props
    node = HTMLNode(props={
        "href": "https://www.google.com",
        "target": "_blank"
    })
    # Note: Order of props might vary because dictionaries don't guarantee order
    # So we need to check for both possible orders
    result = node.props_to_html()
    possibility1 = ' href="https://www.google.com" target="_blank"'
    possibility2 = ' target="_blank" href="https://www.google.com"'
    assert result == possibility1 or result == possibility2

def run_tests():
    test_props_to_html_empty()
    test_props_to_html_single_prop()
    test_props_to_html_multiple_props()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()