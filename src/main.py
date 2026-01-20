from textnode import TextType, TextNode

def main():
    test_variable = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test_variable)
    return None

if __name__ == "__main__":
    main()
