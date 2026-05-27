#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """
   
    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        s = super().__str__()
        if s == '<':
            s = s.replace('<', '&lt;')
        elif s == '>':
            s = s.replace('>', '&gt;')
        elif s == '"':
            s = s.replace('"', '&quot;')
        s = s.replace('\n', '\n<br />\n')
        return s


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self, message='incorrect behaviour'):
            super().__init__(message)

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        if not self.check_type(content):
            raise self.ValidationError
        if attr == {}:
            attr = ''
        if content is None:
            content = ''
        # if isinstance(content, list):
        #     content = '\n  '.join(str(item) for item in content if item != '')
        self.tag = tag
        self.attr = attr
        self.content = content
        self.tag_type = tag_type

    def render(self, level=0):
        indent = '  ' * level
        
        if self.tag_type != 'double':
            return (f"{indent}<{self.tag}{self.attr} />")
        # sans contenu
        if self.content is None or self.content == '':
            return f"{indent}<{self.tag}{self.attr}></{self.tag}>"
        # contenu avec une ou plusieurs Element
        elif isinstance(self.content, Elem):
            child = self.content.render(level + 1)
            return f"{indent}<{self.tag}{self.attr}>\n{child}\n{indent}</{self.tag}>"
        # contenu est une list
        elif isinstance(self.content, list):
            filtered = [item for item in self.content if item != Text('')]
            if not filtered:
                return f"{indent}<{self.tag}{self.attr}></{self.tag}>"
            children = '\n'.join(
                item.render(level + 1) if isinstance(item, Elem) else f"{indent}  {item}"
                for item in filtered
            )
            return f"{indent}<{self.tag}{self.attr}>\n{children}\n{indent}</{self.tag}>"
        else:
            # contenu texte simple
            return f"{indent}<{self.tag}{self.attr}>\n{indent}  {self.content}\n{indent}</{self.tag}>"

    def __str__(self):
        return self.render(0)

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += elem
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (content is None or isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


def main():
      
 print(str(Elem(
        tag='html',
        content=[
            Elem(tag='head', content=Elem(tag='title', content=Text('"Hello ground!"'))),
            Elem(tag='body', content=Elem(tag='h1', content=Text('"Oh no, not again!"'))),
            Elem(tag='img', attr=' src="http://i.imgur.com/pfp3T.jpg"', tag_type='single')
        ]
    )))
if __name__ == '__main__':
    main()
