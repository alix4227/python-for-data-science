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
   
    def check_body_div_content(self, body):
        if isinstance(body.content, Elem):
            if not isinstance(body.content, BODY_ELEMENTS):
                return False
            return self.check_body_div_content(body.content)
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
    
    def check_h1_etc(self, body):
        if isinstance(body, Elem):
            if isinstance(body, TITLE_ETC_ELEMENTS):
                if isinstance(body.content, list):
                    for item in body.content:
                        if not isinstance(item, Text):
                            return False
                        self.text += 1
                    if (self.text > 1):
                        return False
                elif not isinstance(body.content, Text):
                    return False
                self.text = 0
            return self.check_h1_etc(body.content)

        elif isinstance(body, list):
            for item in body:
                self.check_h1_etc(item)
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
        if not self.check_body_div_content(self.element.content[1]):
            return False
        if not self.check_title(self.element.content[0]):
            return False
        if not self.check_h1_etc(self.element.content[1]):
            return False
        return True


    def is_valid(self):
        return(self.checker())

            
    def __str__(self):
        return(f'{str(self.element)}')

def main(): 
    test = Page(Html([
    Head(content=Title()),
    Body(H1([Text('hello')]))
]))
    print(test.is_valid())


if __name__ == '__main__':
    main()