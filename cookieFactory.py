class Cookie:
    def __init__(self):
        pass

    @classmethod
    def create_cookies(cls, cookies_count):
        baking_sheet = []
        for obj in range(0, cookies_count):
            baking_sheet.append(Cookie())
        return baking_sheet
