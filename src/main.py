from textnode import TextNode, TextType

def main():
    obj = TextNode("Ooga booga", TextType.LINK, "https://www.youtube.com/watch?v=XfqOB4hvxlY")
    print(obj)
    
main()