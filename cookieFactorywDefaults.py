class Cookie:
    DEFAULT_SCARF_COLOR = 'Green'
    DEFAULT_BUTTON_COLOR = 'Blue'

    def __init__(self, scarf_color=None, buttons_color=None):
        self.scarf_color = scarf_color or Cookie.DEFAULT_SCARF_COLOR
        self.buttons_color = buttons_color or Cookie.DEFAULT_BUTTON_COLOR

    @classmethod
    def create_cookies(cls, cookies_count, scarf_color=None, buttons_color=None):
        baking_sheet = []
        for obj in range(0, cookies_count):
            baking_sheet.append(Cookie(scarf_color, buttons_color))
        return baking_sheet

print(Cookie.create_cookies(5, scarf_color='red'))
