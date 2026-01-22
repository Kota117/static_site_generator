class HTMLNode():
    def  __init__(self, tag: str = None, value: str = None, children: list["HTMLNode"] = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for key in self.props.keys():
            props_html += f" {key}=\"{self.props[key]}\""
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
