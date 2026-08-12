from elements import*


ELEMENTS = (Html, Head, Body,
Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)
BODY_ELEMENTS = (H1, H2, Div, Table, Ul, Ol, Span, Text)
TITLE_ETC_ELEMENTS = (Title, H1, H2, Li, Th, Td)

class Page():
    def __init__(self, element):
        self.element = element
        self.balises = []
        self.text_title = 0
        self.text = 0
        
    def check_P_and_Span(self, element):
        if element is None or isinstance(element, Text):
            return True
        
        if isinstance(element, P):
            if isinstance(element.content, list):
                for item in element.content:
                    if not isinstance(item, Text):
                        return False
            elif element.content is not None and not isinstance(element.content, Text):
                return False
            return True
        

        if isinstance(element, Span):
            if isinstance(element.content, list):
                for item in element.content:
                    if not isinstance(item, (Text, P)):
                        return False

                    if isinstance(item, P) and not self.check_P_and_Span(item):
                        return False
            elif element.content is not None:
                if not isinstance(element.content, (Text, P)):
                    return False

                if isinstance(element.content, P):
                    if not self.check_P_and_Span(element.content):
                        return False
            return True
        

        if isinstance(element, Elem):
            return self.check_P_and_Span(element.content)
        

        if isinstance(element, list):
            for item in element:
                if not self.check_P_and_Span(item):
                    return False
            return True
        
        return True
    

    def check_Ul_and_Ol(self, element):
        if element is None or isinstance(element, Text):
            return True
        
        if isinstance(element, (Ul, Ol)):
            if isinstance(element.content, list):
                if not element.content:
                    return False
                for item in element.content:
                    if not isinstance(item, Li):
                        return False
            elif not isinstance(element.content, Li):
                return False
            elif element.content is None:
                return False
            return True
        
        if isinstance(element, Elem):
            return self.check_Ul_and_Ol(element.content)
        
        if isinstance(element, list):
            for item in element:
                if not self.check_Ul_and_Ol(item):
                    return False
            return True
        
        return True
    
    def check_Tr(self, element):

        if element is None or isinstance(element, Text):
            return True
        
        if isinstance(element, Tr):
            if isinstance(element.content, list):
                countTh = 0
                countTd = 0
                if not element.content:
                    return False
                for item in element.content:
                    if not isinstance(item, (Td, Th)):
                        return False
                    if isinstance(item, Td):
                        countTd += 1
                    if isinstance(item, Th):
                        countTh += 1
                if countTd  and countTh:
                    return False
            elif not isinstance(element.content, (Td, Th)):
                return False
            elif element.content is None:
                return False
            return True
        
        if isinstance(element, Elem):
            return self.check_Tr(element.content)
        
        if isinstance(element, list):
            for item in element:
                if not self.check_Tr(item):
                    return False
            return True
        
        return True
    
    def check_Table(self, element):

        if element is None or isinstance(element, Text):
            return True
        
        if isinstance(element, Table):
            if isinstance(element.content, list):
                for item in element.content:
                    if not isinstance(item, Tr):
                        return False
            elif not isinstance(element.content, Tr):
                return False
            return True
        
        if isinstance(element, Elem):
            return self.check_Table(element.content)
        
        if isinstance(element, list):
            for item in element:
                if not self.check_Table(item):
                    return False
            return True
        
        return True


    def check_title_in_head(self):
        title = 0
        head_block = str(self.element.content[0])
        balises = [tag.split('>')[0].lstrip('/') for tag in head_block.split('<')[1:]]
        for item in balises:
            if item not in ('head', 'title'):
                return (False)
            if item in ('title'):
                title += 1
        return (title == 2)
   
    def check_body_content(self, body):
        if body is None or body == '' or isinstance(body, Text):
            return True
        if isinstance(body, Elem):
            content = body.content
            if content in (None, '') or isinstance(content, Text):
                return True
            if isinstance(content, list):
                for item in content:
                    if not isinstance(item, BODY_ELEMENTS):
                        return False
                return True
            return isinstance(content, BODY_ELEMENTS)
        if isinstance(body, list):
            for item in body:
                if not self.check_body_content(item):
                    return False
            return True
        return False
    
    def check_div_content(self, element):
        if element is None or element == '' or isinstance(element, Text):
            return True
        
        if isinstance(element, Div):
            content = element.content
            if content in (None, '') or isinstance(content, Text):
                return True
            if isinstance(content, list):
                for item in content:
                    if not isinstance(item, BODY_ELEMENTS):
                        return False
                return True
            return isinstance(content, BODY_ELEMENTS)

        if isinstance(element, Elem):
            return self.check_div_content(element.content)

        if isinstance(element, list):
            for item in element:
                if not self.check_div_content(item):
                    return False
            return True
        return True
    
    def check_title(self, head):
        if isinstance(head, Elem):
            if isinstance(head, Title):
                if isinstance(head.content, Text):
                    self.text_title += 1
                if isinstance(head.content, list):
                    for item in head.content:
                        if isinstance(item, Text):
                            self.text_title += 1
            return self.check_title(head.content)
        return (self.text_title <= 1)
    
    def check_h1_etc(self, element):
        if element is None or isinstance(element, Text):
            return True
        
        if isinstance(element, TITLE_ETC_ELEMENTS):
            if isinstance(element.content, list):
                count_text = 0
                for item in element.content:
                    if isinstance(item, Elem) and not isinstance(item, Text):
                        return False
                    count_text += 1
                if count_text > 1:
                    return False
            elif isinstance(element.content, Elem) and not isinstance(element.content, Text):
                return False
            return True
        
        if isinstance(element, Elem):
            return self.check_h1_etc(element.content)
        
        if isinstance(element, list):
            for item in element:
                if not self.check_h1_etc(item):
                    return False
            return True
        return True


    def check_body_and_head(self):
        html_page = self.element
        self.balises = [tag.split('>')[0].lstrip('/') for tag in str(html_page).split('<')[1:]]
        body = head = 0
        if self.balises[0] != 'html':
            return False
        if self.balises[1] != 'head':
            return False
        for item in self.balises:
            if item == 'head':
                head += 1
            if item == 'body':
                body += 1
        return (body == 2 and head == 2)

    def check_elements(self, html_page):
        if isinstance(html_page, Text):
            return True
        if html_page in (None, ''):
            return True
        if isinstance(html_page, ELEMENTS):
            return self.check_elements(html_page.content)
        if isinstance(html_page, list):
            for item in html_page:
                if not self.check_elements(item):
                    return False
            return True
        return False
    

    def checker(self):
        html_page = self.element
        if not self.check_body_and_head():
            return False
        if not self.check_elements(html_page):
            return False
        if not self.check_title_in_head():
            return False
        if not self.check_body_content(self.element.content[1]):
            return False
        if not self.check_div_content(self.element.content[1]):
            return False
        if not self.check_title(self.element.content[0]):
            return False
        if not self.check_h1_etc(self.element.content[1]):
            return False
        if not self.check_P_and_Span(self.element.content[1]):
            return False
        if not self.check_Ul_and_Ol(self.element.content[1]):
            return False
        if not self.check_Tr(self.element.content[1]):
            return False
        if not self.check_Table(self.element.content[1]):
            return False
        return True


    def is_valid(self):
        return(self.checker())
    
    def write_to_file(self, filename):
        if not isinstance(filename, str):
            return False
        with open(filename, 'w') as file:
            if isinstance(self.element, Html):
                file.write(f'<!DOCTYPE html>\n{str(self.element)}')
            else:
                file.write(f'{str(self.element)}')

            
    def __str__(self):
        if isinstance(self.element, Html):
            return(f'<!DOCTYPE html>\n{str(self.element)}')
        return(f'{str(self.element)}')

def main():
    tests = [
        (
            "valid page",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Div([
                    Table([
                        Tr([Th(Text("Name")), Th(Text("Age"))]),
                        Tr([Td(Text("Alix")), Td(Text("100"))]),
                    ], attr=' style="border: 1px solid black; border-collapse: collapse;"')
                ]))
            ])),
            True
        ),
        (
            "invalid unknown node type",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Test(Text("bad")))
            ])),
            False
        ),
        (
            "invalid html order",
            Page(Html([
                Body(Div(Text("bad"))),
                Head(Title(Text("Hello World!")))
            ])),
            False
        ),
        (
            "invalid html with extra head",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Head(Title(Text("Second title"))),
                Body(Div(Text("content")))
            ])),
            False
        ),
        (
            "invalid head with extra element",
            Page(Html([
                Head([Title(Text("Hello World!")), Meta()]),
                Body(Div(Text("content")))
            ])),
            False
        ),
        (
            "invalid title with two texts",
            Page(Html([
                Head(Title([Text("Hello"), Text("World")])),
                Body(Div(Text("content")))
            ])),
            False
        ),
        (
            "invalid body with p",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(P(Text("not allowed")))
            ])),
            False
        ),
        (
            "invalid div with p",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Div(P(Text("not allowed"))))
            ])),
            False
        ),
        (
            "valid span with p",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Span([Text("hello"), P(Text("world"))]))
            ])),
            True
        ),
        (
            "invalid p with div",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Div(P([Text("hello"), Div(Text("bad"))])))
            ])),
            False
        ),
        (
            "empty body",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body()
            ])),
            True
        ),
        (
            "empty div",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Div())
            ])),
            True
        ),
        (
            "invalid ul empty",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Ul())
            ])),
            False
        ),
        (
            "valid ul with li",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Ul([Li(Text("item"))]))
            ])),
            True
        ),
        (
            "invalid title twice",
            Page(Html([
                Head([
                    Title(Text("Hello")),
                    Title(Text("World"))
                ]),
                Body(Div(Text("content")))
            ])),
            False
        ),
        (
            "invalid ul with non-li",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Ul([Li(Text("ok")), Div(Text("bad"))]))
            ])),
            False
        ),
        (
            "valid ol with li",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Ol([Li(Text("first")), Li(Text("second"))]))
            ])),
            True
        ),
        (
            "invalid ol with non-li",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Ol([Li(Text("ok")), Div(Text("bad"))]))
            ])),
            False
        ),
        (
            "valid tr with th",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Table([
                    Tr([Th(Text("Name")), Th(Text("Age"))])
                ]))
            ])),
            True
        ),
        (
            "valid tr with td",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Table([
                    Tr([Td(Text("Alix")), Td(Text("100"))])
                ]))
            ])),
            True
        ),
        (
            "invalid table row mixed td/th",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Table([
                    Tr([Th(Text("Name")), Td(Text("Age"))])
                ]))
            ])),
            False
        ),
        (
            "invalid tr empty",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Table([
                    Tr()
                ]))
            ])),
            False
        ),
        (
            "invalid table with div",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Table([
                    Div(Text("bad"))
                ]))
            ])),
            False
        ),
        (
            "valid h1 with text",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(H1(Text("Heading")))
            ])),
            True
        ),
        (
            "invalid h1 with two texts",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(H1([Text("one"), Text("two")]))
            ])),
            False
        ),
        (
            "invalid td with two texts",
            Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Table([
                    Tr([Td([Text("one"), Text("two")])])
                ]))
            ])),
            False
        ),
    ]

    for name, page, expected in tests:
        result = page.is_valid()
        status = "OK" if result == expected else "FAIL"
        print(f"{status} - {name}: expected={expected}, got={result}")

    page = Page(Html([
                Head(Title(Text("Hello World!"))),
                Body(Div([
                    Table([
                        Tr([Th(Text("Name")), Th(Text("Age"))]),
                        Tr([Td(Text("Alix")), Td(Text("100"))]),
                    ], attr=' style="border: 1px solid black; border-collapse: collapse;"')
                ]))
            ]))
    print(page)
    page.write_to_file("test.html")

    page2 = Page(Body(Div(Text("bad"))))
    print(page2)
    page2.write_to_file("test2.html")

if __name__ == '__main__':
    main()