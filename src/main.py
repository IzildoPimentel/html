from textnode import TextNode, TextType

print("hello world")

def main():
    print("hello world")
    node = TextNode("Click here for bootdev", TextType.LINK, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()