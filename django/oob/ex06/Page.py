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
                if not element.content:
                    return False
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
   
    def check_body_div_content(self, body):
        if isinstance(body.content, (Div)):
            return self.check_body_div_content(body.content)
        elif isinstance(body.content, (Elem)):
            if not isinstance(body.content, BODY_ELEMENTS):
                return False
            return self.check_body_div_content(body.content)
        elif isinstance(body.content, list):
            for item in body.content:
                if not isinstance(item, BODY_ELEMENTS):
                    return False 
                if not self.check_body_div_content(item):
                    return False
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
                if not self.check_h1_etc(item):
                    return False
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
        # if not self.check_body_and_head():
        #     return False
        # if not self.check_elements(html_page):
        #     return False
        # if not self.check_title_in_head():
        #     return False
        # if not self.check_body_div_content(self.element.content[1]):
        #     return False
        # if not self.check_title(self.element.content[0]):
        #     return False
        # if not self.check_h1_etc(self.element.content[1]):
        #     return False
        # if not self.check_P_and_Span(self.element.content[1]):
        #     return False
        # if not self.check_Ul_and_Ol(self.element.content[1]):
        #     return False
        if not self.check_Tr(self.element.content[1]):
            return False
        if not self.check_Table(self.element.content[1]):
            return False
        return True


    def is_valid(self):
        return(self.checker())

            
    def __str__(self):
        return(f'{str(self.element)}')

def main(): 
    test = Page(Html([
    Head(content=Title()),
    Body(Div([Tr([Th()])]))
]))
    print(test.is_valid())


if __name__ == '__main__':
    main()