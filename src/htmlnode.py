class HTMLNode:
    def __init__(self,*,tag=None,value=None,children=None,props=None): #children should be a list of HTMLNode type objects
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop_out = ""
        if not self.props:
            return prop_out
        for prop in self.props:
            prop_out = prop_out + " " + prop + "=\"" + self.props[prop] + "\""
        return prop_out
    
    def __repr__(self): #test this with nested children to see how it looks.  It looks bad :(  solution: we don't print the children.
        return f"tag: <{self.tag}>, value: {self.value}, props: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self,*,tag=None,value,props=None):
        super().__init__(tag=tag,value=value,props=props,children=None)

    def to_html(self):
        if not self.value:
            raise ValueError("leaf node requires a value")
        if not self.tag:
            return self.value
        if not self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, *, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("no tag provided to ParentNode object")
        if len(self.children)==0:
            raise ValueError("no children in ParentNode object")
        html_out = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html_out += child.to_html()
        html_out += f"</{self.tag}>"
        return html_out