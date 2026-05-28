from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='html', attr=attr, content=content, tag_type=tag_type)


class Head(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='head', attr=attr, content=content, tag_type=tag_type)


class Body(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='body', attr=attr, content=content, tag_type=tag_type)


class Title(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='title', attr=attr, content=content, tag_type=tag_type)


class Meta(Elem):
    def __init__(self, content=None, attr={}, tag_type='single'):
        super().__init__(tag='meta', attr=attr, content=content, tag_type=tag_type)


class Img(Elem):
    def __init__(self, content=None, attr={}, tag_type='single'):
        super().__init__(tag='img', attr=attr, content=content, tag_type=tag_type)


class Table(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='table', attr=attr, content=content, tag_type=tag_type)


class Th(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='th', attr=attr, content=content, tag_type=tag_type)


class Tr(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='tr', attr=attr, content=content, tag_type=tag_type)


class Td(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='td', attr=attr, content=content, tag_type=tag_type)


class Ul(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='ul', attr=attr, content=content, tag_type=tag_type)


class Ol(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='ol', attr=attr, content=content, tag_type=tag_type)


class Li(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='li', attr=attr, content=content, tag_type=tag_type)


class H1(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='h1', attr=attr, content=content, tag_type=tag_type)


class H2(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='h2', attr=attr, content=content, tag_type=tag_type)


class P(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='p', attr=attr, content=content, tag_type=tag_type)


class Div(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='div', attr=attr, content=content, tag_type=tag_type)


class Span(Elem):
    def __init__(self, content=None, attr={}, tag_type='double'):
        super().__init__(tag='span', attr=attr, content=content, tag_type=tag_type)


class Hr(Elem):
    def __init__(self, content=None, attr={}, tag_type='single'):
        super().__init__(tag='hr', attr=attr, content=content, tag_type=tag_type)


class Br(Elem):
    def __init__(self, content=None, attr={}, tag_type='single'):
        super().__init__(tag='br', attr=attr, content=content, tag_type=tag_type)


def main(): 
    print( Html( [Head(), Body()] ) ) 
    print( Html([Head(Title(Text('"Hello ground!"'))), Body([H1(Text('"Oh no, not again!"')), Img(attr=' src="http://i.imgur.com/pfp3T.jpg"')])]) )

if __name__ == '__main__':
    main()