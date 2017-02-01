class Cookie(object):
    DEFAULT_BUTTON_COLOR = 'Blue'
    DEFAULT_SCARF_COLOR = 'Green'

    def __init__(self, scarf_color=None, buttons_color=None):
        self.scarf_color = scarf_color or Cookie.DEFAULT_SCARF_COLOR
        self.buttons_color = buttons_color or Cookie.DEFAULT_BUTTON_COLOR

